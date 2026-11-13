# Load from ~/.zshrc to enable repository commands.
function runcode() {
    local repo=/Users/laptopheaven/competitive-programming
    if [[ "$PWD" != "$repo" && "$PWD" != "$repo/"* ]]; then
        print -u2 'Run runcode from the competitive-programming folder.'
        return 1
    fi
    python3 "$repo/scripts/runcode.py" "$@"
}

function push() {
    local repo=/Users/laptopheaven/competitive-programming
    if [[ "$1" != this ]]; then
        print -u2 'Usage: push this [commit message]'
        return 1
    fi
    if [[ "$PWD" != "$repo" && "$PWD" != "$repo/"* ]]; then
        print -u2 'Run push this from the competitive-programming folder.'
        return 1
    fi
    shift
    local message="${*:-Update competitive programming solutions}"
    git -C "$repo" add -A || return $?
    if ! git -C "$repo" diff --cached --quiet; then
        git -C "$repo" commit -m "$message" || return $?
    fi
    git -C "$repo" push origin HEAD
}
