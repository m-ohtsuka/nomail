Summary: Nomail - offline SMTP server
Summary(ja): Nomail - オフライン SMTP サーバ
Name: nomail
Version: 0.4.11
Release: 1
Group: System Environment/Daemons
Source: ftp://ftp.KU3G.org/pub/nomail/%{name}-%{version}.tar.gz
URL: http://www.KU3G.org/negi/nomail/
Copyright: GPL
Provides: smtpdaemon
Requires: procmail perl
Prereq: /usr/sbin/useradd
Obsoletes: sendmail
BuildArchitectures: noarch
BuildRoot: /var/tmp/%{name}-%{version}-root

%description
The Nomail is a SMTP server for use with dial-up internet links.

%description -l ja
Nomail はダイアルアップ・モバイル環境の為のオフラインメールサー
バです。ローカル宛メールはそのまま配信しますが，自ホスト以外の
メールは明示的に nosend を実行するまでキューに溜め続けるので，
ネットワークが繋っていない状態でもメールを送ることができます。

%prep
%setup -q

%build

%install
mkdir -p $RPM_BUILD_ROOT{/usr/bin,/usr/sbin,/usr/man/ja/man8,/etc}
mkdir -p $RPM_BUILD_ROOT/var/spool/nomail
mkdir -p $RPM_BUILD_ROOT/etc/nomail
cp nomail $RPM_BUILD_ROOT/usr/sbin
(cd $RPM_BUILD_ROOT/usr/sbin ; ln -s nomail sendmail)
cp nosend $RPM_BUILD_ROOT/usr/bin
cp nomail.conf $RPM_BUILD_ROOT/etc/nomail
cp *.8 $RPM_BUILD_ROOT/usr/man/ja/man8
gzip -9 $RPM_BUILD_ROOT/usr/man/ja/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

%pre
useradd -M -o -r -d /dev/null -s /dev/null \
	-c "Nomail SMTP server" nomail >/dev/null 2>&1 || :

%post
echo '###############################################################'
echo 'please add /etc/inetd.conf below entry and restart inetd'
echo 'smtp    stream  tcp     nowait  nomail  /usr/sbin/tcpd  nomail'
echo '###############################################################'

%postun
if [ $1 = 0 ] ; then
	userdel nomail >/dev/null 2>&1 || :
fi

%files
%defattr(-,root,root)
%config /etc/nomail/nomail.conf
%attr(4711,nomail,nomail) /usr/sbin/nomail
/usr/sbin/sendmail
%attr(4711,nomail,nomail) /usr/bin/nosend
%attr(0700,nomail,nomail) /var/spool/nomail
/usr/man/ja/man8/*
%doc COPYING ChangeLog FAQ INSTALL README VERSION nomail.txt nosend.txt
