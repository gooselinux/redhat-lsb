# Define this to link to which library version  eg. /lib64/ld-lsb-x86-64.so.3
%define lsbsover 3 

%ifarch %{ix86}
%define ldso ld-linux.so.2
%define lsbldso ld-lsb.so
%endif

%ifarch ia64
%define ldso ld-linux-ia64.so.2
%define lsbldso ld-lsb-ia64.so
%endif

%ifarch ppc
%define ldso ld.so.1
%define lsbldso ld-lsb-ppc32.so
%endif

%ifarch ppc64
%define ldso ld64.so.1
%define lsbldso ld-lsb-ppc64.so
%endif

%ifarch s390
%define ldso ld.so.1
%define lsbldso ld-lsb-s390.so
%endif

%ifarch s390x
%define ldso ld64.so.1
%define lsbldso ld-lsb-s390x.so
%endif

%ifarch x86_64
%define ldso ld-linux-x86-64.so.2
%define lsbldso ld-lsb-x86-64.so
%endif

%ifarch ia64 ppc64 s390x x86_64
%define qual ()(64bit)
%else
%define qual %{nil}
%endif

%define upstreamlsbrelver 2.0
%define lsbrelver 4.0
%define srcrelease 1

Summary: LSB base libraries support for Red Hat Enterprise Linux
Name: redhat-lsb
Version: 4.0
Release: 2.1%{?dist}
URL: http://www.linuxfoundation.org/collaborate/workgroups/lsb
Source0: %{name}-%{version}-%{srcrelease}.tar.bz2
#Source1: http://prdownloads.sourceforge.net/lsb/lsb-release-%{upstreamlsbrelver}.tar.gz
Patch0: lsb-release-3.1-update-init-functions.patch
Patch1: redhat-lsb-lsb_start_daemon-fix.patch
Patch2: redhat-lsb-trigger.patch
License: GPL
Group: System Environment/Base
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: glibc-static
# dependency for primary LSB application for v1.3
Provides: lsb = %{version}
# dependency for primary LSB application for v2.0 and v3.0
%ifarch %{ix86}
%define archname ia32
%endif
%ifarch ia64
%define archname ia64
%endif
%ifarch ppc
%define archname ppc32
%endif
%ifarch ppc64
%define archname ppc64
%endif
%ifarch s390
%define archname s390
%endif
%ifarch s390x
%define archname s390x
%endif
%ifarch x86_64
%define archname amd64
%endif
Provides: lsb-core-%{archname} = %{version}
Provides: lsb-core-noarch = %{version}

ExclusiveArch: %{ix86} ia64 x86_64 ppc ppc64 s390 s390x

%ifarch %{ix86}
# archLSB IA32 Base Libraries
Requires: libc.so.6
Requires: libcrypt.so.1
Requires: libdl.so.2
Requires: libgcc_s.so.1
Requires: libm.so.6
Requires: libncurses.so.5
Requires: libpthread.so.0
Requires: libstdc++.so.6
Requires: libutil.so.1
Requires: libz.so.1
%endif

%ifarch ia64
# archLSB IA64 Base Libraries
Requires: libc.so.6.1()(64bit)
Requires: libcrypt.so.1()(64bit)
Requires: libdl.so.2()(64bit)
Requires: libgcc_s.so.1()(64bit)
Requires: libm.so.6.1()(64bit)
Requires: libncurses.so.5()(64bit)
Requires: libpthread.so.0()(64bit)
Requires: libstdc++.so.6()(64bit)
Requires: libutil.so.1()(64bit)
Requires: libz.so.1()(64bit)
%endif

%ifarch ppc
# archLSB PPC32 Base Libraries
Requires: libc.so.6
Requires: libcrypt.so.1
Requires: libdl.so.2
Requires: libgcc_s.so.1
Requires: libm.so.6
Requires: libncurses.so.5
Requires: libpthread.so.0
Requires: libstdc++.so.6
Requires: libutil.so.1
Requires: libz.so.1
%endif

%ifarch ppc64
# archLSB PPC64 Base Libraries
Requires: libc.so.6()(64bit)
Requires: libcrypt.so.1()(64bit)
Requires: libdl.so.2()(64bit)
Requires: libgcc_s.so.1()(64bit)
Requires: libm.so.6()(64bit)
Requires: libncurses.so.5()(64bit)
Requires: libpthread.so.0()(64bit)
Requires: libstdc++.so.6()(64bit)
Requires: libutil.so.1()(64bit)
Requires: libz.so.1()(64bit)
%endif

%ifarch s390
# archLSB S390 Base Libraries
Requires: libc.so.6
Requires: libcrypt.so.1
Requires: libdl.so.2
Requires: libgcc_s.so.1
Requires: libm.so.6
Requires: libncurses.so.5
Requires: libpthread.so.0
Requires: libstdc++.so.6
Requires: libutil.so.1
Requires: libz.so.1
%endif

%ifarch s390x
# archLSB S390X Base Libraries
Requires: libc.so.6()(64bit)
Requires: libcrypt.so.1()(64bit)
Requires: libdl.so.2()(64bit)
Requires: libgcc_s.so.1()(64bit)
Requires: libm.so.6()(64bit)
Requires: libncurses.so.5()(64bit)
Requires: libpthread.so.0()(64bit)
Requires: libstdc++.so.6()(64bit)
Requires: libutil.so.1()(64bit)
Requires: libz.so.1()(64bit)
%endif

%ifarch x86_64
# archLSB AMD64 Base Libraries
Requires: libc.so.6()(64bit)
Requires: libcrypt.so.1()(64bit)
Requires: libdl.so.2()(64bit)
Requires: libgcc_s.so.1()(64bit)
Requires: libm.so.6()(64bit)
Requires: libncurses.so.5()(64bit)
Requires: libpthread.so.0()(64bit)
Requires: libstdc++.so.6()(64bit)
Requires: libutil.so.1()(64bit)
Requires: libz.so.1()(64bit)
%endif

# gLSB Base/Utility/Stdc++
Requires: libcrypt.so.1%{qual}
Requires: libdl.so.2%{qual}
Requires: libgcc_s.so.1%{qual}
Requires: libncurses.so.5%{qual}
Requires: libnspr4.so%{qual}
Requires: libnss3.so%{qual}
Requires: libpam.so.0%{qual}
Requires: libpthread.so.0%{qual}
Requires: librt.so.1%{qual}
Requires: libssl3.so%{qual}
Requires: libstdc++.so.6%{qual}
Requires: libutil.so.1%{qual}
Requires: libz.so.1%{qual}

# gLSB Command and Utilities
Requires: /bin/awk
Requires: /bin/basename
Requires: /bin/cat
Requires: /bin/chgrp
Requires: /bin/chmod
Requires: /bin/chown
Requires: /bin/cp
Requires: /bin/cpio
Requires: /bin/cut
Requires: /bin/date
Requires: /bin/dd
Requires: /bin/df
Requires: /bin/dmesg
Requires: /bin/echo
Requires: /bin/ed
Requires: /bin/egrep
Requires: /bin/env
Requires: /bin/false
Requires: /bin/fgrep
Requires: /bin/find
Requires: /bin/gettext
Requires: /bin/grep
Requires: /bin/gunzip
Requires: /bin/gzip
Requires: /bin/hostname
Requires: /bin/kill
Requires: /bin/ln
Requires: /bin/ls
Requires: /bin/mailx
Requires: /bin/mkdir
Requires: /bin/mknod
Requires: /bin/mktemp
Requires: /bin/more
Requires: /bin/mount
Requires: /bin/mv
Requires: /bin/nice
Requires: /bin/ps
Requires: /bin/pwd
Requires: /bin/rm
Requires: /bin/rmdir
Requires: /bin/sed
Requires: /bin/sh
Requires: /bin/sleep
Requires: /bin/sort
Requires: /bin/stty
Requires: /bin/su
Requires: /bin/sync
Requires: /bin/tar
Requires: /bin/touch
Requires: /bin/true
Requires: /bin/umount
Requires: /bin/uname
Requires: /bin/zcat
Requires: /sbin/fuser
Requires: /sbin/pidof
Requires: /sbin/shutdown
Requires: /usr/bin/[
Requires: /usr/bin/ar
Requires: /usr/bin/at
Requires: /usr/bin/batch
Requires: /usr/bin/bc
Requires: /usr/bin/chfn
Requires: /usr/bin/chsh
Requires: /usr/bin/cksum
Requires: /usr/bin/cmp
Requires: /usr/bin/col
Requires: /usr/bin/comm
Requires: /usr/bin/crontab
Requires: /usr/bin/csplit
Requires: /usr/bin/diff
Requires: /usr/bin/dirname
Requires: /usr/bin/du
Requires: /usr/bin/expand
Requires: /usr/bin/expr
Requires: /usr/bin/file
Requires: /usr/bin/fold
Requires: /usr/bin/gencat
Requires: /usr/bin/getconf
Requires: /usr/bin/groups
Requires: /usr/bin/head
Requires: /usr/bin/iconv
Requires: /usr/bin/id
Requires: /usr/bin/install
Requires: /usr/bin/ipcrm
Requires: /usr/bin/ipcs
Requires: /usr/bin/join
Requires: /usr/bin/killall
Requires: /usr/bin/locale
Requires: /usr/bin/localedef
Requires: /usr/bin/logger
Requires: /usr/bin/logname
Requires: /usr/bin/m4
Requires: /usr/bin/make
Requires: /usr/bin/man
Requires: /usr/bin/md5sum
Requires: /usr/bin/mkfifo
Requires: /usr/bin/msgfmt
Requires: /usr/bin/newgrp
Requires: /usr/bin/nl
Requires: /usr/bin/nohup
Requires: /usr/bin/od
Requires: /usr/bin/passwd
Requires: /usr/bin/paste
Requires: /usr/bin/patch
Requires: /usr/bin/pathchk
Requires: /usr/bin/pax
Requires: /usr/bin/perl
Requires: /usr/bin/pr
Requires: /usr/bin/printf
Requires: /usr/bin/python
Requires: /usr/bin/renice
Requires: /usr/bin/seq
Requires: /usr/bin/split
Requires: /usr/bin/strip
Requires: /usr/bin/tail
Requires: /usr/bin/tee
Requires: /usr/bin/test
Requires: /usr/bin/time
Requires: /usr/bin/tr
Requires: /usr/bin/tsort
Requires: /usr/bin/tty
Requires: /usr/bin/unexpand
Requires: /usr/bin/uniq
Requires: /usr/bin/wc
Requires: /usr/bin/xargs
Requires: /usr/lib/lsb/install_initd
Requires: /usr/lib/lsb/remove_initd
Requires: /usr/sbin/groupadd
Requires: /usr/sbin/groupdel
Requires: /usr/sbin/groupmod
Requires: /usr/sbin/sendmail
Requires: /usr/sbin/useradd
Requires: /usr/sbin/userdel
Requires: /usr/sbin/usermod

%description
The Linux Standard Base (LSB) is an attempt to develop a set of
standards that will increase compatibility among Linux distributions.
The redhat-lsb package provides utilities needed for LSB Compliant
Applications.  It also contains requirements that will ensure that all
components required by the LSB that are provided by Red Hat Linux are
installed on the system.

%package graphics
Group: System Environment/Base
Summary: LSB graphics libraries support for Red Hat Enterprise Linux

Provides: lsb-graphics-%{archname} = %{version}
Provides: lsb-graphics-noarch = %{version}

%description graphics
The Linux Standard Base (LSB) Graphics Specifications define components that are required
 to be present on an LSB conforming system.

%ifarch %{ix86}
# archLSB IA32 Graphics Libraries
Requires: libatk-1.0.so.0
Requires: libgdk-x11-2.0.so.0
Requires: libgdk_pixbuf-2.0.so.0
Requires: libgdk_pixbuf_xlib-2.0.so.0
Requires: libglib-2.0.so.0
Requires: libgmodule-2.0.so.0
Requires: libgobject-2.0.so.0
Requires: libgthread-2.0.so.0
Requires: libgtk-x11-2.0.so.0
Requires: libpango-1.0.so.0
Requires: libpangocairo-1.0.so.0
Requires: libpangoft2-1.0.so.0
Requires: libpangoxft-1.0.so.0
Requires: libqt-mt.so.3
Requires: libQtCore.so.4
Requires: libQtGui.so.4
Requires: libQtNetwork.so.4
Requires: libQtOpenGL.so.4
Requires: libQtSql.so.4
Requires: libQtSvg.so.4
Requires: libQtXml.so.4
%endif

%ifarch ia64
# archLSB IA64 Graphics Libraries
Requires: libatk-1.0.so.0()(64bit)
Requires: libgdk-x11-2.0.so.0()(64bit)
Requires: libgdk_pixbuf-2.0.so.0()(64bit)
Requires: libgdk_pixbuf_xlib-2.0.so.0()(64bit)
Requires: libglib-2.0.so.0()(64bit)
Requires: libgmodule-2.0.so.0()(64bit)
Requires: libgobject-2.0.so.0()(64bit)
Requires: libgthread-2.0.so.0()(64bit)
Requires: libgtk-x11-2.0.so.0()(64bit)
Requires: libpango-1.0.so.0()(64bit)
Requires: libpangocairo-1.0.so.0()(64bit)
Requires: libpangoft2-1.0.so.0()(64bit)
Requires: libpangoxft-1.0.so.0()(64bit)
Requires: libqt-mt.so.3()(64bit)
Requires: libQtCore.so.4()(64bit)
Requires: libQtGui.so.4()(64bit)
Requires: libQtNetwork.so.4()(64bit)
Requires: libQtOpenGL.so.4()(64bit)
Requires: libQtSql.so.4()(64bit)
Requires: libQtSvg.so.4()(64bit)
Requires: libQtXml.so.4()(64bit)
%endif

%ifarch ppc
# archLSB PPC32 Graphics Libraries
Requires: libatk-1.0.so.0
Requires: libgdk-x11-2.0.so.0
Requires: libgdk_pixbuf-2.0.so.0
Requires: libgdk_pixbuf_xlib-2.0.so.0
Requires: libglib-2.0.so.0
Requires: libgmodule-2.0.so.0
Requires: libgobject-2.0.so.0
Requires: libgthread-2.0.so.0
Requires: libgtk-x11-2.0.so.0
Requires: libpango-1.0.so.0
Requires: libpangocairo-1.0.so.0
Requires: libpangoft2-1.0.so.0
Requires: libpangoxft-1.0.so.0
Requires: libqt-mt.so.3
Requires: libQtCore.so.4
Requires: libQtGui.so.4
Requires: libQtNetwork.so.4
Requires: libQtOpenGL.so.4
Requires: libQtSql.so.4
Requires: libQtSvg.so.4
Requires: libQtXml.so.4
%endif

%ifarch ppc64
# archLSB PPC64 Graphics Libraries
Requires: libatk-1.0.so.0()(64bit)
Requires: libgdk-x11-2.0.so.0()(64bit)
Requires: libgdk_pixbuf-2.0.so.0()(64bit)
Requires: libgdk_pixbuf_xlib-2.0.so.0()(64bit)
Requires: libglib-2.0.so.0()(64bit)
Requires: libgmodule-2.0.so.0()(64bit)
Requires: libgobject-2.0.so.0()(64bit)
Requires: libgthread-2.0.so.0()(64bit)
Requires: libgtk-x11-2.0.so.0()(64bit)
Requires: libpango-1.0.so.0()(64bit)
Requires: libpangocairo-1.0.so.0()(64bit)
Requires: libpangoft2-1.0.so.0()(64bit)
Requires: libpangoxft-1.0.so.0()(64bit)
Requires: libqt-mt.so.3()(64bit)
Requires: libQtCore.so.4()(64bit)
Requires: libQtGui.so.4()(64bit)
Requires: libQtNetwork.so.4()(64bit)
Requires: libQtOpenGL.so.4()(64bit)
Requires: libQtSql.so.4()(64bit)
Requires: libQtSvg.so.4()(64bit)
Requires: libQtXml.so.4()(64bit)
%endif

%ifarch s390
# archLSB S390 Graphics Libraries
Requires: libatk-1.0.so.0
Requires: libgdk-x11-2.0.so.0
Requires: libgdk_pixbuf-2.0.so.0
Requires: libgdk_pixbuf_xlib-2.0.so.0
Requires: libglib-2.0.so.0
Requires: libgmodule-2.0.so.0
Requires: libgobject-2.0.so.0
Requires: libgthread-2.0.so.0
Requires: libgtk-x11-2.0.so.0
Requires: libpango-1.0.so.0
Requires: libpangocairo-1.0.so.0
Requires: libpangoft2-1.0.so.0
Requires: libpangoxft-1.0.so.0
Requires: libqt-mt.so.3
Requires: libQtCore.so.4
Requires: libQtGui.so.4
Requires: libQtNetwork.so.4
Requires: libQtOpenGL.so.4
Requires: libQtSql.so.4
Requires: libQtSvg.so.4
Requires: libQtXml.so.4
%endif

%ifarch s390x
# archLSB S390X Graphics Libraries
Requires: libatk-1.0.so.0()(64bit)
Requires: libgdk-x11-2.0.so.0()(64bit)
Requires: libgdk_pixbuf-2.0.so.0()(64bit)
Requires: libgdk_pixbuf_xlib-2.0.so.0()(64bit)
Requires: libglib-2.0.so.0()(64bit)
Requires: libgmodule-2.0.so.0()(64bit)
Requires: libgobject-2.0.so.0()(64bit)
Requires: libgthread-2.0.so.0()(64bit)
Requires: libgtk-x11-2.0.so.0()(64bit)
Requires: libpango-1.0.so.0()(64bit)
Requires: libpangocairo-1.0.so.0()(64bit)
Requires: libpangoft2-1.0.so.0()(64bit)
Requires: libpangoxft-1.0.so.0()(64bit)
Requires: libqt-mt.so.3()(64bit)
Requires: libQtCore.so.4()(64bit)
Requires: libQtGui.so.4()(64bit)
Requires: libQtNetwork.so.4()(64bit)
Requires: libQtOpenGL.so.4()(64bit)
Requires: libQtSql.so.4()(64bit)
Requires: libQtSvg.so.4()(64bit)
Requires: libQtXml.so.4()(64bit)
%endif

%ifarch x86_64
# archLSB AMD64 Graphics Libraries
Requires: libatk-1.0.so.0()(64bit)
Requires: libgdk-x11-2.0.so.0()(64bit)
Requires: libgdk_pixbuf-2.0.so.0()(64bit)
Requires: libgdk_pixbuf_xlib-2.0.so.0()(64bit)
Requires: libglib-2.0.so.0()(64bit)
Requires: libgmodule-2.0.so.0()(64bit)
Requires: libgobject-2.0.so.0()(64bit)
Requires: libgthread-2.0.so.0()(64bit)
Requires: libgtk-x11-2.0.so.0()(64bit)
Requires: libpango-1.0.so.0()(64bit)
Requires: libpangocairo-1.0.so.0()(64bit)
Requires: libpangoft2-1.0.so.0()(64bit)
Requires: libpangoxft-1.0.so.0()(64bit)
Requires: libpthread.so.0()(64bit)
Requires: libqt-mt.so.3()(64bit)
Requires: libQtCore.so.4()(64bit)
Requires: libQtGui.so.4()(64bit)
Requires: libQtNetwork.so.4()(64bit)
Requires: libQtOpenGL.so.4()(64bit)
Requires: libQtSql.so.4()(64bit)
Requires: libQtSvg.so.4()(64bit)
Requires: libQtXml.so.4()(64bit)
%endif

# gLSB Graphics Libraries
Requires: libasound.so.2%{qual}
Requires: libatk-1.0.so.0%{qual}
Requires: libcairo.so.2%{qual}
Requires: libcrypt.so.1%{qual}
Requires: libcups.so.2%{qual}
Requires: libcupsimage.so.2%{qual}
Requires: libfontconfig.so.1%{qual}
Requires: libfreetype.so.6%{qual}
Requires: libgdk-x11-2.0.so.0%{qual}
Requires: libgdk_pixbuf-2.0.so.0%{qual}
Requires: libgdk_pixbuf_xlib-2.0.so.0%{qual}
Requires: libGL.so.1%{qual}
Requires: libglib-2.0.so.0%{qual}
Requires: libGLU.so.1%{qual}
Requires: libgmodule-2.0.so.0%{qual}
Requires: libgobject-2.0.so.0%{qual}
Requires: libgthread-2.0.so.0%{qual}
Requires: libgtk-x11-2.0.so.0%{qual}
Requires: libICE.so.6%{qual}
Requires: libjpeg.so.62%{qual}
Requires: libpango-1.0.so.0%{qual}
Requires: libpangocairo-1.0.so.0%{qual}
Requires: libpangoft2-1.0.so.0%{qual}
Requires: libpangoxft-1.0.so.0%{qual}
Requires: libpng12.so.0%{qual}
Requires: libqt-mt.so.3%{qual}
Requires: libQtCore.so.4%{qual}
Requires: libQtGui.so.4%{qual}
Requires: libQtNetwork.so.4%{qual}
Requires: libQtOpenGL.so.4%{qual}
Requires: libQtSql.so.4%{qual}
Requires: libQtSvg.so.4%{qual}
Requires: libQtXml.so.4%{qual}
Requires: libSM.so.6%{qual}
Requires: libX11.so.6%{qual}
Requires: libXext.so.6%{qual}
Requires: libXft.so.2%{qual}
Requires: libXi.so.6%{qual}
Requires: libxml2.so.2%{qual}
Requires: libXrender.so.1%{qual}
Requires: libXt.so.6%{qual}
Requires: libXtst.so.6%{qual}

# gLSB Graphics Command and Utilities
Requires: /usr/bin/fc-cache
Requires: /usr/bin/fc-list
Requires: /usr/bin/fc-match



%package printing
Group: System Environment/Base
Summary: LSB printing libraries support for Red Hat Enterprise Linux

Provides: lsb-printing-%{archname} = %{version}
Provides: lsb-printing-noarch = %{version}

%description printing
The Linux Standard Base (LSB) Printing Specifications define components that are required
 to be present on an LSB conforming system.

# gLSB Printing Libraries
Requires: libcups.so.2%{qual}
Requires: libcupsimage.so.2%{qual}

# gLSB Printing Command and Utilities
Requires: /usr/bin/foomatic-rip
Requires: /usr/bin/gs
Requires: /usr/bin/lp
Requires: /usr/bin/lpr


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0 -b .triggerfix

%build
cd lsb-release-%{upstreamlsbrelver}
make

%pre
# remove the extra symlink /bin/mailx -> /bin/mail
if [ -e /bin/mailx ]; then
   if [ -L /bin/mailx ]; then
     rm -f /bin/mailx
   fi 
fi


%install
rm -rf $RPM_BUILD_ROOT
# LSB uses /usr/lib rather than /usr/lib64 even for 64bit OS
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir} $RPM_BUILD_ROOT/%{_lib} $RPM_BUILD_ROOT%{_mandir} \
         $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT/usr/lib/lsb \
         $RPM_BUILD_ROOT%{_sysconfdir}/lsb-release.d/ $RPM_BUILD_ROOT%{_sbindir}
make DESTDIR=$RPM_BUILD_ROOT install
cd lsb-release-%{upstreamlsbrelver}
make mandir=$RPM_BUILD_ROOT/%{_mandir} prefix=$RPM_BUILD_ROOT/%{_prefix} install
cd ..
touch $RPM_BUILD_ROOT/etc/lsb-release.d/core-4.0-%{archname}
touch $RPM_BUILD_ROOT/etc/lsb-release.d/core-4.0-noarch
touch $RPM_BUILD_ROOT/etc/lsb-release.d/graphics-4.0-%{archname}
touch $RPM_BUILD_ROOT/etc/lsb-release.d/graphics-4.0-noarch
touch $RPM_BUILD_ROOT/etc/lsb-release.d/printing-4.0-%{archname}
touch $RPM_BUILD_ROOT/etc/lsb-release.d/printing-4.0-noarch

#touch $RPM_BUILD_ROOT/etc/lsb-release.d/core-3.2-%{archname}
#touch $RPM_BUILD_ROOT/etc/lsb-release.d/core-3.2-noarch
#touch $RPM_BUILD_ROOT/etc/lsb-release.d/desktop-3.2-%{archname}
#touch $RPM_BUILD_ROOT/etc/lsb-release.d/desktop-3.2-noarch
# and claim LSB 3.1 is supported as well
#touch $RPM_BUILD_ROOT/etc/lsb-release.d/core-3.1-%{archname}
#touch $RPM_BUILD_ROOT/etc/lsb-release.d/core-3.1-noarch
#touch $RPM_BUILD_ROOT/etc/lsb-release.d/desktop-3.1-%{archname}
#touch $RPM_BUILD_ROOT/etc/lsb-release.d/desktop-3.1-noarch

for LSBVER in %{lsbsover}; do
  ln -s %{ldso} $RPM_BUILD_ROOT/%{_lib}/%{lsbldso}.$LSBVER
done

mkdir -p $RPM_BUILD_ROOT/bin

# LSB uses /usr/lib rather than /usr/lib64 even for 64bit OS
# According to the lsb-core documentation provided by 
# http://refspecs.linux-foundation.org/LSB_3.2.0/LSB-Core-generic/LSB-Core-generic.pdf
# it's OK to put non binary in /usr/lib.
ln -snf ../../../sbin/chkconfig $RPM_BUILD_ROOT/usr/lib/lsb/install_initd
ln -snf ../../../sbin/chkconfig $RPM_BUILD_ROOT/usr/lib/lsb/remove_initd
#ln -snf mail $RPM_BUILD_ROOT/bin/mailx

#mkdir -p $RPM_BUILD_ROOT/usr/X11R6/lib/X11/xserver
#ln -snf /usr/%{_lib}/xserver/SecurityPolicy $RPM_BUILD_ROOT/usr/X11R6/lib/X11/xserver/SecurityPolicy
#ln -snf /usr/share/X11/fonts $RPM_BUILD_ROOT/usr/X11R6/lib/X11/fonts
#ln -snf /usr/share/X11/rgb.txt  $RPM_BUILD_ROOT/usr/X11R6/lib/X11/rgb.txt

# According to https://bugzilla.redhat.com/show_bug.cgi?id=232918 , the '-static' option
# is imported against segfault error while running redhat_lsb_trigger
gcc $RPM_OPT_FLAGS -Os -static -fno-stack-protector -o redhat_lsb_trigger{.%{_target_cpu},.c} -DLSBSOVER='"%{lsbsover}"' \
  -DLDSO='"%{ldso}"' -DLSBLDSO='"/%{_lib}/%{lsbldso}"' -D_GNU_SOURCE
install -m 700 redhat_lsb_trigger.%{_target_cpu} \
  $RPM_BUILD_ROOT%{_sbindir}/redhat_lsb_trigger.%{_target_cpu}

cp -p redhat_lsb_init $RPM_BUILD_ROOT/bin/redhat_lsb_init

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- glibc
if [ -x /usr/sbin/redhat_lsb_trigger.%{_target_cpu} ]; then
  /usr/sbin/redhat_lsb_trigger.%{_target_cpu}
fi

%ifnarch %{ix86}
  /sbin/sln %{ldso} /%{_lib}/%{lsbldso} || :
%else
  if [ -f /emul/ia32-linux/lib/%{ldso} ]; then
    for LSBVER in %{lsbsover}; do
      /sbin/sln /emul/ia32-linux/lib/%{ldso} /%{_lib}/%{lsbldso}.$LSBVER || :
    done
  else
    for LSBVER in %{lsbsover}; do
      /sbin/sln %{ldso} /%{_lib}/%{lsbldso}.$LSBVER || :
    done
  fi
%endif

%ifarch %{ix86}
%post
# make this softlink again for /emul
  if [ -f /emul/ia32-linux/lib/%{ldso} ]; then
    for LSBVER in %{lsbsover}; do
      /sbin/sln /emul/ia32-linux/lib/%{ldso} /%{_lib}/%{lsbldso}.$LSBVER || :
    done
  fi
%endif

%files
%defattr(-,root,root)
%{_sysconfdir}/redhat-lsb
%dir %{_sysconfdir}/lsb-release.d
# These files are needed because they shows which LSB we're supporting now, 
# for example, if core-3.1-noarch exists, it means we are supporting LSB3.1 now
%{_sysconfdir}/lsb-release.d/*
%{_mandir}/*/*
%{_bindir}/*
#/bin/mailx
/bin/redhat_lsb_init
/usr/lib/lsb
/%{_lib}/*so*
/lib/lsb*
%{_sbindir}/redhat_lsb_trigger.%{_target_cpu}

%files graphics
%defattr(-,root,root)
%{_sysconfdir}/lsb-release.d/graphics*

%files printing
%defattr(-,root,root)
%{_sysconfdir}/lsb-release.d/printing*


%changelog
* Fri Jan 15 2010 Lawrence Lim <llim@redhat.com> - 4.0-2.1
- Resolves: Bug 506540

* Fri Jan 15 2010 Lawrence Lim <llim@redhat.com> - 4.0-2
- update spec file to split package into core, desktop and printing (Curtis Doty, #472633)

* Fri Jan 8 2010 Lawrence Lim <llim@redhat.com> - 4.0-1
- update to LSB4.0

* Tue Oct 27 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 3.2-7
- apply fix from bz514760 (thanks to Jakub Jelinek)

* Wed Oct 21 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 3.2-6
- apply fix from bz485367 (thanks to Jon Thomas)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 24 2009 Jens Petersen <petersen@redhat.com>
- improve url to LSB WG

* Thu Apr 23 2009 Jens Petersen <petersen@redhat.com> - 3.2-4
- use dist tag (Debarshi, #496553)
- update to ix86 (caillon)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug 28 2008 Hao Liu <hliu@redhat.com> 3.2-2
- Modify "Requires: /usr/bin/mailx" to "Requires: mailx" (Bug #460249)

* Wed Aug 18 2008 Hao Liu <hliu@redhat.com> 3.2-1
- Port forward to LSB 3.2
- Remove symlink for mailx if user is upgrading from the redhat-lsb of older version 
- Since F10 put mailx under /usr/bin, change the corresponding requires

* Thu Aug 5 2008 Hao Liu <hliu@redhat.com> - 3.1-22
- Remove 2 requires which provided by redhat-lsb
- Add comments explaining why hard-coded path is kept
- Resolve some hard-coded path problems
- Add comments explaining why importing '-static' option while compiling redhat_lsb_trigger
- Replace %{_libdir}/lsb with /usr/lib/lsb
- Replace /%{_lib}/* with /%{_lib}/*so*
- Replace /lib/lsb with /lib/lsb*

* Thu Jul 31 2008 Lawrence Lim <llim@redhat.com> - 3.1-21
- remove symlink for mailx (Bug #457241)

* Wed Apr 16 2008 Mats Wichmann <mats@freestandards.org> 3.2-1
- port forward to LSB 3.2

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.1-20
- Autorebuild for GCC 4.3

* Wed Oct 3 2007 Lawrence Lim <llim@redhat.com> - 3.1-19
- fix build issue on ppc - (.opd+0x10): multiple definition of `__libc_start_main'

* Fri Sep 21 2007 Lawrence Lim <llim@redhat.com> - 3.1-18
- fix build issue in minimal build root (Bug #265241)

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 3.1-17
- Rebuild for selinux ppc32 issue.

* Fri Aug 20 2007 Lawrence Lim <llim@redhat.com> - 3.1-16
- update spec file in accordance to feedback provided through merge review - merge-review.patch - #226363

* Wed Jul 18 2007 Lawrence Lim <llim@redhat.com> - 3.1-15.f8
- Resolved: #239842 - /lib/lsb/init-functions shall use aliases but not functions
- forward port the patch from 3.1-12.3.EL which fix #217566, #233530, #240916

* Wed Jul 2 2007 Lawrence Lim <llim@redhat.com> - 3.1-14.fc7
- fixed Bug 232918 for new glibc version

* Tue Jun 26 2007 Lawrence Lim <llim@redhat.com> - 3.1-12.3.EL
- Resolves: #217566 - rewrite /lib/lsb/init-functions file needs to define the commands as true shell functions rather than aliases.
- Resolves: #233530 - LSB pidofproc misspelled as pidofprof.
- Resolves: #240916 - "log_warning_message" replaced with "log_warning_msg" per the LSB 3.1 spec

* Wed Dec 6 2006 Lawrence Lim <llim@redhat.com> - 3.1-12.2.EL
- Resolves: bug 217566
- revise patch

* Wed Nov 29 2006 Lawrence Lim <llim@redhat.com> - 3.1-12
- replaced aliases with functions in /lib/lsb/init-functions; Bug 217566

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 3.1-11
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Thu Sep 21 2006 Lawrence Lim <llim@redhat.com> - 3.1-10.3
- Fix upgrade issue; Bug 202548 

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3.1-10.2.1
- rebuild

* Thu Jul 6 2006 Lawrence Lim <llim@redhat.com> - 3.1-10.2
- for some strange reason, ld-lsb-x86-64.so need to be ld-lsb-x86-64.so.3 (LSB3.0) rather than ld-lsb-x86-64.so.3.1 (LSB3.1)

* Thu Jul 6 2006 Lawrence Lim <llim@redhat.com> - 3.1-10.1
- generate spec file on RHEL5-Alpha system
- fix vsw4 test suite setup by creating symlink for X11 SecurityPolicy and XFontPath

* Thu Jun 22 2006 Lawrence Lim <llim@redhat.com> - 3.0-10
- Rewrite most part of the mkredhat-lsb to obtain information directly via specdb 
  rather than sniffing through sgml
- remove redundent script and bump up tarball version

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 3.0-9.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 3.0-9.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Jan 13 2006 Leon Ho <llch@redhat.com> 3.0-9
- Migrated back to rawhide

* Wed Aug  3 2005 Leon Ho <llch@redhat.com> 3.0-8.EL
- Added libstdc++.so.6/libGL.so.1 requirement (RH#154605)

* Wed Aug  3 2005 Leon Ho <llch@redhat.com> 3.0-7.EL
- Fixed multilib problem on lsb_release not to read /etc/lsb-release and solely
  depends on /etc/lsb-release.d/ (Advised by LSB committee)
- Removed /etc/lsb-release (Advised by LSB committee)

* Mon Aug  1 2005 Leon Ho <llch@redhat.com> 3.0-6.EL
- Made the /etc/lsb-release useful (RH#154605)
- Added redhat_lsb_trigger to fix RH#160585 (Jakub Jelinek)
- Fixed AMD64 base libraries requirement parsing (RH#154605)

* Tue Jul 26 2005 Leon Ho <llch@redhat.com> 3.0-5.EL
- Fixed redhat-lsb's mkredhat-lsb on fetching lib and 
  cmd requirements

* Mon Jul 18 2005 Leon Ho <llch@redhat.com> 3.0-4.EL
- Rebuilt

* Tue Jul 05 2005 Leon Ho <llch@redhat.com> 3.0-3.EL
- Disabled support for LSB 1.3 and 2.0

* Mon Jun 20 2005 Leon Ho <llch@redhat.com> 3.0-2.EL
- Upgraded to lsb-release 2.0

* Thu Jun 09 2005 Leon Ho <llch@redhat.com> 3.0-1.EL
- Moved to LSB 3.0

* Wed Apr 13 2005 Leon Ho <llch@redhat.com> 1.3-10
- Fixed ix86 package with ia32 emul support 

* Tue Feb 01 2005 Leon Ho <llch@redhat.com> 1.3-9
- Sync what we have changed on the branches
  Wed Nov 24 2004 Harald Hoyer <harald@redhat.com>
  - added post section to recreate the softlink in emul mode (bug 140739)
  Mon Nov 15 2004 Phil Knirsch <pknirsch@redhat.com>
  Tiny correction of bug in new triggers

* Mon Jan 24 2005 Leon Ho <llch@redhat.com> 1.3-8
- Add support provide on lsb-core-* for each arch

* Fri Jan 21 2005 Leon Ho <llch@redhat.com> 1.3-7
- Add to support multiple LSB test suite version
- Add %endif in trigger postun

* Thu Nov 11 2004 Phil Knirsch <pknirsch@redhat.com> 1.3-6
- Fixed invalid sln call for trigger in postun on ia64 (#137647)

* Mon Aug 09 2004 Phil Knirsch <pknirsch@redhat.com> 1.3-4
- Bump release and rebuilt for RHEL4.

* Thu Jul 24 2003 Matt Wilson <msw@redhat.com> 1.3-3
- fix lsb ld.so name for ia64 (#100613)

* Fri May 23 2003 Matt Wilson <msw@redhat.com> 1.3-2
- use /usr/lib/lsb for install_initd, remove_initd

* Fri May 23 2003 Matt Wilson <msw@redhat.com> 1.3-2
- add ia64 x86_64 ppc ppc64 s390 s390x

* Tue Feb 18 2003 Matt Wilson <msw@redhat.com> 1.3-1
- 1.3

* Wed Sep  4 2002 Matt Wilson <msw@redhat.com>
- 1.2.0

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Mar 27 2002 Matt Wilson <msw@redhat.com>
- addeed trigger on glibc to re-establish the ld-lsb.so.1 symlink in the
  forced downgrade case.

* Tue Mar 12 2002 Bill Nottingham <notting@redhat.com>
- add initscripts support

* Thu Jan 24 2002 Matt Wilson <msw@redhat.com>
- Initial build.

