import click
from git import Repo

FORMAT = '* {hash} {message}'


def _find_tag(repo, tag_name):
    return next((tag for tag in repo.tags if tag.name == tag_name), None)


def _find_latest_tag(repo):
    latest_authored_date = 0
    latest_tag = None
    for tag in repo.tags:
        if tag.commit.authored_date > latest_authored_date:
            latest_authored_date = tag.commit.authored_date
            latest_tag = tag

    return latest_tag


def _resolve_tag(repo, tag_name):
    if not tag_name:
        return None

    tag = _find_tag(repo, tag_name)
    if tag is None:
        raise click.ClickException(f'tag not found: {tag_name}')

    return tag


@click.command()
@click.argument('path', type=click.Path(dir_okay=True, file_okay=False, exists=True))
@click.option('--start-tag', help='Start changelog after this tag.')
@click.option('--end-tag', help='End changelog at this tag (defaults to HEAD).')
def cli(path, start_tag, end_tag):
    repo = Repo(path)
    if end_tag and not start_tag:
        raise click.ClickException('--end-tag requires --start-tag')

    resolved_start_tag = _resolve_tag(repo, start_tag) or _find_latest_tag(repo)
    resolved_end_tag = _resolve_tag(repo, end_tag)
    end_ref = resolved_end_tag.name if resolved_end_tag else 'HEAD'

    if resolved_start_tag:
        commits = list(repo.iter_commits(f'{resolved_start_tag.name}..{end_ref}', first_parent=True))
    else:
        commits = list(repo.iter_commits(end_ref, first_parent=True))

    commits.reverse()

    for commit in commits:
        print(FORMAT.format(hash=commit.hexsha, message=commit.message.strip().splitlines()[0]))


if __name__ == '__main__':
    cli()
