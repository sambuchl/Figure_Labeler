for dir in ./*/     # list directories in the form "/tmp/dirname/"
do
        dir=${dir%*/}      # remove the trailing "/"
        echo "${dir##*/}"
        ls "${dir##*/}" | wc -l    # print everything after the final "/"
        done
