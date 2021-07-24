case $1 in
    pylint)
        find . -type f -name '*.py' -exec python3 -m pylint {} \;
        ;;
    *)
        echo -n "UNKNOWN"
        ;;
esac
