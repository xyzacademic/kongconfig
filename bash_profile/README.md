Instructions
=

Just copy lines you think useful in `bashrc` into your `~/.bashrc.`
Some useful alias commands are in `alias-bashrc`. Modify some dir paths
on your need.

`shopt -s expand_aliases` is very important. Just copy it into your 
`~/.bashrc`

1. Create a bash file like `.alias-bashrc` in your home directory.
2. Copy commands from `alias-bashrc` to your '.alias-bashrc'.
3. Add `shopt -s expand_aliases` and `source ~/.alias-bashrc` to the end of 
your `.bashrc` in your home directory. So it will activate `.alias-bashrc` 
whenever your terminal or submitted job starts.

If you include everything in `alias-bashrc` in your `.alias-bashrc`, you will 
have these convenient commands:
    
    Node412  # qlogin to node 412
    Check  # check all jobs running status under datasci and datasci3
    Gpu  #  Check every node' GPU running status.
    python  # run my anaconda python, you will have my python environment
    ipython  # you will have my ipython environment
    
To make command `Gpu` works. You have to put `kong_tools` in your home directory,
and modify its path in `alias-bashrc`. Read `README.md` in `kong_tools`, you 
also need to modify a path in `gpu_status.sh`