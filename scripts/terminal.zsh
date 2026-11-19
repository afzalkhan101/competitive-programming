# Compatible with zsh and bash. Commands resolve this clone from the current folder.
function _practice_repo() {
    local repo
    repo="$(git rev-parse --show-toplevel 2>/dev/null)" || return 1
    if [[ ! -f "$repo/practice/catalog.json" || ! -f "$repo/scripts/cf.py" ]]; then
        printf '%s\n' 'Run this command inside your competitive-programming clone.' >&2
        return 1
    fi
    printf '%s\n' "$repo"
}

function _practice_python() {
    local repo="$1"
    shift
    if [[ -x "$repo/.venv/bin/python" ]]; then
        "$repo/.venv/bin/python" "$@"
    else
        python3 "$@"
    fi
}

function runcode() {
    local repo
    repo="$(_practice_repo)" || return 1
    _practice_python "$repo" "$repo/scripts/runcode.py" "$@"
}

function cf() {
    local repo
    repo="$(_practice_repo)" || return 1
    _practice_python "$repo" "$repo/scripts/cf.py" "$@"
}

function testcode() {
    cf test "$@"
}

function push() {
    if [[ "$1" != this ]]; then
        printf '%s\n' 'Usage: push this [commit message]' >&2
        return 1
    fi
    shift
    cf push "$*"
}

function submit() {
    cf submit "$@"
}
