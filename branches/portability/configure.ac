#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ(2.12)
AC_INIT([freQ Jabber bot], [1.1.199-svn], [mailto:kreved-at-kreved.org])
AC_CONFIG_MACRO_DIR([m4])

AC_PROG_INSTALL


AM_PATH_PYTHON([2.5])
if test "x$PYTHON" = "x:"; then
        AC_MSG_ERROR([Python not found])
fi

AC_OUTPUT([Makefile] [doc/Makefile] [tools/freqtool])
