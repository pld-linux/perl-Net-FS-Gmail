#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Net
%define	pnam	FS-Gmail
Summary:	Net::FS::Gmail - store and retrieve files on Gmail
Summary(pl.UTF-8):	Net::FS::Gmail - zapis i odczyt plików z Gmaila
Name:		perl-Net-FS-Gmail
Version:	0.2
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e07e6b7dc2b97c0a4229ade19901e6e6
URL:		http://search.cpan.org/dist/Net-FS-Gmail/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Mail-Webmail-Gmail >= 1.05.1
BuildRequires:	perl-Time-modules
BuildRequires:	perl-URI
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl module that allows using Gmail as file storage.

%description -l pl.UTF-8
Ten moduł Perla umożliwia używanie Gmaila jako przestrzeni dyskowej.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build
sed -ie 's#!perl#!/usr/bin/perl#' bin/gmailfs

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL README TODO
%attr(755,root,root) %{_bindir}/gmailfs
%{perl_vendorlib}/Net/FS/*.pm
%{_mandir}/man[13]/*
