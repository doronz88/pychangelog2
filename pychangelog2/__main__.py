import click
from git import Repo

FORMAT = '* {hash} {message}'


@click.command()
@click.argument('path', type=click.Path(dir_okay=True, file_okay=False, exists=True))
def cli(path):
    repo = Repo(path)

    last_authored_date = 0
    last_tag = None
    for tag in repo.tags:
        if tag.commit.authored_date > last_authored_date:
            last_authored_date = tag.commit.authored_date
            last_tag = tag

    commits = []
    for commit in repo.iter_commits():
        if commit == last_tag.commit:
            # reaches last tag
            break

        if len(commit.parents) > 1:
            commit = commit.parents[1]

        if commit not in commits:
            commits.append(commit)

    commits = commits[::-1]

    for commit in commits:
        print(FORMAT.format(hash=commit.hexsha, message=commit.message.strip().splitlines()[0]))


if __name__ == '__main__':
    cli()
