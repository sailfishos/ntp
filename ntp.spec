Summary: The NTP daemon and utilities
Name: ntp
Version: 4.2.4p8
Release: 1
# primary license (COPYRIGHT) : MIT
# ElectricFence/ (not used) : GPLv2
# kernel/sys/ppsclock.h (not used) : BSD with advertising
# include/ntif.h (not used) : BSD
# include/rsa_md5.h : BSD with advertising
# include/ntp_rfc2553.h : BSD with advertising
# libisc/inet_aton.c (not used) : BSD with advertising
# libntp/md5c.c : BSD with advertising
# libntp/mktime.c : BSD with advertising
# libntp/ntp_random.c : BSD with advertising
# libntp/memmove.c : BSD with advertising
# libntp/ntp_rfc2553.c : BSD with advertising
# libntp/adjtimex.c (not used) : BSD
# libopts/ : BSD or GPLv2+
# libparse/ : BSD
# ntpd/refclock_jjy.c: MIT
# ntpd/refclock_oncore.c : BEERWARE License (aka, Public Domain)
# ntpd/refclock_palisade.c : BSD with advertising
# ntpd/refclock_jupiter.c : BSD with advertising
# ntpd/refclock_mx4200.c : BSD with advertising
# ntpd/refclock_palisade.h : BSD with advertising
# ntpstat-0.2/ : GPLv2
# util/ansi2knr.c (not used) : GPL+
# sntp/ (not packaged) : MSNTP
License: (MIT and BSD and BSD with advertising) and GPLv2
Group: System Environment/Daemons
Source0: http://www.eecis.udel.edu/~ntp/ntp_spool/ntp4/ntp-4.2/ntp-%{version}.tar.gz
Source1: ntp.conf
Source2: ntp.keys
Source4: ntpd.sysconfig
Source5: ntpstat-0.2.tgz
Source6: ntp.step-tickers
Source8: ntp.cryptopw
Source9: ntpdate.sysconfig
Source10: ntp.dhclient

# ntpbz #628, #1073
Patch1: ntp-4.2.4p4-kernel.patch
# add support for dropping root to ntpdate
Patch2: ntp-4.2.4p0-droproot.patch
# ntpbz #812
Patch3: ntp-4.2.4-groups.patch
# ntpbz #1170
Patch4: ntp-4.2.4p7-daemonpll.patch
# link ntpd with -ffast-math on ia64
Patch5: ntp-4.2.4-linkfastmath.patch
# ntpbz #1134
Patch6: ntp-4.2.4p2-tentative.patch
# ntpbz #897
Patch7: ntp-4.2.4p2-noseed.patch
# ntpbz #830
Patch8: ntp-4.2.4p4-multilisten.patch
# fix script used to generate man pages
Patch9: ntp-4.2.4-html2man.patch
# ntpbz #898
Patch10: ntp-4.2.4p5-htmldoc.patch
# fixed in 4.2.5
Patch11: ntp-4.2.4p2-filegen.patch
# ntpbz #738
Patch12: ntp-4.2.4-sprintf.patch
# use editline instead of readline
Patch13: ntp-4.2.4p8-editline.patch
# add option -m to lock memory
Patch14: ntp-4.2.4p8-mlock.patch
# fixed in 4.2.5
Patch15: ntp-4.2.4p2-clockselect.patch
# don't build sntp
Patch16: ntp-4.2.4p8-nosntp.patch
# ntpbz #802
Patch17: ntp-4.2.4p7-sleep.patch
# ntpbz #779, #823
Patch18: ntp-4.2.4p7-bcast.patch
# ntpbz #759
Patch19: ntp-4.2.4p0-retcode.patch
# ntpbz #397
Patch20: ntp-4.2.4p2-noif.patch
# force IPv6 support
Patch21: ntp-4.2.4p7-ipv6.patch
# align buffer for control messages
Patch22: ntp-4.2.4p4-cmsgalign.patch
# force use of clock_gettime
Patch23: ntp-4.2.4p8-gettime.patch
# reload resolv.conf after failure in name resolution
Patch24: ntp-4.2.4p4-resinit.patch
# ntpbz #992
Patch25: ntp-4.2.4p5-rtnetlink.patch
# don't log STA_MODE (PLL/FLL) changes
Patch26: ntp-4.2.4p7-stamode.patch
# ntpbz #808
Patch27: ntp-4.2.4p5-driftonexit.patch
# add missing nanokernel macros
Patch28: ntp-4.2.4p7-nano.patch
# allow minpoll 3 as in 4.2.5
Patch29: ntp-4.2.4p7-minpoll.patch
# fix frequency mode, backported from 4.2.5
Patch30: ntp-4.2.4p7-freqmode.patch
# handle unknown clock types
Patch31: ntpstat-0.2-clksrc.patch
# process first packet in multipacket response
Patch32: ntpstat-0.2-multipacket.patch
#CVE-2014-9293
Patch33: CVE-2014-9293.patch
#CVE-2014-9294
Patch34: CVE-2014-9294.patch
#CVE-2014-9295
Patch35: CVE-2014-9295.patch
#ntp-4.2.4p8-lcrypto.patch
Patch36: ntp-4.2.4p8-lcrypto.patch

URL: http://www.ntp.org
Requires: ntpdate = %{version}-%{release}
BuildRequires: libcap-devel openssl-devel libedit-devel perl-HTML-Parser

%description
The Network Time Protocol (NTP) is used to synchronize a computer's
time with another reference time source. This package includes ntpd
(a daemon which continuously adjusts system time) and utilities used
to query and configure the ntpd daemon.

Perl scripts ntp-wait and ntptrace are in the ntp-perl package and
the ntpdate program is in the ntpdate package. The documentation is
in the ntp-doc package.

%package perl
Summary: NTP utilities written in perl
Group: Applications/System
Requires: %{name} = %{version}-%{release}
# perl introduced in 4.2.4p4-7
Obsoletes: %{name} < 4.2.4p4-7
%description perl
This package contains perl scripts ntp-wait and ntptrace.
 
%package -n ntpdate
Summary: Utility to set the date and time via NTP
Group: Applications/System
Requires(pre): shadow-utils 

%description -n ntpdate
ntpdate is a program for retrieving the date and time from
NTP servers.

%package doc
Summary: NTP documentation
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
This package contains NTP documentation in HTML format.
 
%define ntpdocdir %{_datadir}/doc/%{name}-%{version}

# pool.ntp.org vendor zone which will be used in ntp.conf
%if 0%{!?vendorzone:1}
%define vendorzone meego.
%endif

%prep 
%setup -q -a 5

%patch1 -p1 -b .kernel
%patch2 -p1 -b .droproot
%patch3 -p1 -b .groups
%patch4 -p1 -b .daemonpll
%patch6 -p1 -b .tentative
%patch7 -p1 -b .noseed
%patch8 -p1 -b .multilisten
%patch9 -p1 -b .html2man
%patch10 -p1 -b .htmldoc
%patch11 -p1 -b .filegen
%patch12 -p1 -b .sprintf
%patch13 -p1 -b .editline
%patch14 -p1 -b .mlock
%patch15 -p1 -b .clockselect
%patch16 -p1 -b .nosntp
%patch17 -p1 -b .sleep
%patch18 -p1 -b .bcast
%patch19 -p1 -b .retcode
%patch20 -p1 -b .noif
%patch21 -p1 -b .ipv6
%patch22 -p1 -b .cmsgalign
%patch24 -p1 -b .resinit
%patch25 -p1 -b .rtnetlink
%patch26 -p1 -b .stamode
%patch27 -p1 -b .driftonexit
%patch28 -p1 -b .nano
%patch29 -p1 -b .minpoll
%patch30 -p1 -b .freqmode
%patch31 -p1 -b .clksrc
%patch32 -p1 -b .multipacket
%patch33 -p1 -b .CVE-2014-9293
%patch34 -p1 -b .CVE-2014-9294
%patch35 -p1 -b .CVE-2014-9295
%patch36 -p1 -b .lcrypto

# clock_gettime needs -lrt
sed -i.gettime 's|^LIBS = @LIBS@|& -lrt|' ntp{d,q,dc,date}/Makefile.in
%patch23 -p1 -b .gettime

%ifarch ia64
%patch5 -p1 -b .linkfastmath
%endif

for f in COPYRIGHT; do
	iconv -f iso8859-1 -t utf8 -o ${f}{_,} && touch -r ${f}{,_} && mv -f ${f}{_,}
done

%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
if echo 'int main () { return 0; }' | gcc -pie -fPIE -O2 -xc - -o pietest 2>/dev/null; then
	./pietest && export CFLAGS="$CFLAGS -pie -fPIE"
	rm -f pietest
fi
%configure \
	--sysconfdir=%{_sysconfdir}/ntp/crypto \
	--with-openssl-libdir=%{_libdir} \
	--enable-all-clocks --enable-parse-clocks \
	--enable-linuxcaps
echo '#define KEYFILE "%{_sysconfdir}/ntp/keys"' >> ntpdate/ntpdate.h
echo '#define NTP_VAR "%{_localstatedir}/log/ntpstats/"' >> config.h

make %{?_smp_mflags}

sed -i 's|$ntpq = "ntpq"|$ntpq = "%{_sbindir}/ntpq"|' scripts/ntptrace
sed -i 's|ntpq -c |%{_sbindir}/ntpq -c |' scripts/ntp-wait

pushd html
../scripts/html2man
# remove adjacent blank lines
sed -i 's/^[\t\ ]*$//;/./,/^$/!d' man/man*/*.[58]
popd 

make -C ntpstat-0.2 CFLAGS="$CFLAGS"

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT bindir=%{_sbindir} install

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man{5,8}
rm -rf $RPM_BUILD_ROOT%{_mandir}/man1

pushd ntpstat-0.2
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 ntpstat $RPM_BUILD_ROOT%{_bindir}
install -m 644 ntpstat.1 $RPM_BUILD_ROOT%{_mandir}/man8/ntpstat.8
popd

# fix section numbers
sed -i 's/\(\.TH[a-zA-Z ]*\)[1-9]\(.*\)/\18\2/' $RPM_BUILD_ROOT%{_mandir}/man8/*.8
cp -r html/man/man[58] $RPM_BUILD_ROOT%{_mandir}

mkdir -p $RPM_BUILD_ROOT%{ntpdocdir}
cp -p COPYRIGHT ChangeLog NEWS $RPM_BUILD_ROOT%{ntpdocdir}

# prepare html documentation
find html | egrep '\.(html|css|txt|jpg|gif)$' | grep -v '/build/\|sntp' | \
	cpio -pmd $RPM_BUILD_ROOT%{ntpdocdir}
find $RPM_BUILD_ROOT%{ntpdocdir} -type f | xargs chmod 644
find $RPM_BUILD_ROOT%{ntpdocdir} -type d | xargs chmod 755

pushd $RPM_BUILD_ROOT
mkdir -p .%{_sysconfdir}/{ntp/crypto,sysconfig,dhcp/dhclient.d}
mkdir -p .%{_localstatedir}/{lib/ntp,log/ntpstats}
touch .%{_localstatedir}/lib/ntp/drift
sed -e 's|VENDORZONE\.|%{vendorzone}|' \
	-e 's|ETCNTP|%{_sysconfdir}/ntp|' \
	-e 's|VARNTP|%{_localstatedir}/lib/ntp|' \
	< %{SOURCE1} > .%{_sysconfdir}/ntp.conf
touch -r %{SOURCE1} .%{_sysconfdir}/ntp.conf
install -p -m600 %{SOURCE2} .%{_sysconfdir}/ntp/keys
install -p -m644 %{SOURCE4} .%{_sysconfdir}/sysconfig/ntpd
install -p -m644 %{SOURCE9} .%{_sysconfdir}/sysconfig/ntpdate
install -p -m644 %{SOURCE6} .%{_sysconfdir}/ntp/step-tickers
install -p -m600 %{SOURCE8} .%{_sysconfdir}/ntp/crypto/pw
install -p -m755 %{SOURCE10} .%{_sysconfdir}/dhcp/dhclient.d/ntp.sh
popd

%clean
rm -rf $RPM_BUILD_ROOT

%pre -n ntpdate
/usr/sbin/groupadd -g 38 ntp  2> /dev/null || :
/usr/sbin/useradd -u 38 -g 38 -s /sbin/nologin -M -r -d %{_sysconfdir}/ntp ntp 2>/dev/null || :

%files
%defattr(-,root,root)
%dir %{ntpdocdir}
%{ntpdocdir}/COPYRIGHT
%{ntpdocdir}/ChangeLog
%{ntpdocdir}/NEWS
%{_sbindir}/ntp-keygen
%{_sbindir}/ntpd
%{_sbindir}/ntpdc
%{_sbindir}/ntpq
%{_sbindir}/ntptime
%{_sbindir}/tickadj
%config(noreplace) %{_sysconfdir}/sysconfig/ntpd
%config(noreplace) %{_sysconfdir}/ntp.conf
%dir %attr(750,root,ntp) %{_sysconfdir}/ntp/crypto
%config(noreplace) %{_sysconfdir}/ntp/crypto/pw
%dir %{_sysconfdir}/dhcp/dhclient.d
%{_sysconfdir}/dhcp/dhclient.d/ntp.sh
%dir %attr(-,ntp,ntp) %{_localstatedir}/lib/ntp
%ghost %attr(644,ntp,ntp) %{_localstatedir}/lib/ntp/drift
%dir %attr(-,ntp,ntp) %{_localstatedir}/log/ntpstats
%{_bindir}/ntpstat
%{_mandir}/man5/*.5*
%{_mandir}/man8/ntp-keygen.8*
%{_mandir}/man8/ntpd.8*
%{_mandir}/man8/ntpdc.8*
%{_mandir}/man8/ntpq.8*
%{_mandir}/man8/ntpstat.8*
%{_mandir}/man8/ntptime.8*

%files perl
%defattr(-,root,root)
%{_sbindir}/ntp-wait
%{_sbindir}/ntptrace
%{_mandir}/man8/ntptrace.8*

%files -n ntpdate
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/sysconfig/ntpdate
%dir %{_sysconfdir}/ntp
%config(noreplace) %{_sysconfdir}/ntp/keys
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/ntp/step-tickers
%{_sbindir}/ntpdate
%{_mandir}/man8/ntpdate.8*

%files doc
%defattr(-,root,root)
%{ntpdocdir}/html

