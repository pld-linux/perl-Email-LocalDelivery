#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	LocalDelivery
Summary:	Email::LocalDelivery - deliver a piece of email - simply
Summary(pl):	Email::LocalDelivery - po prostu dostarczanie poczty
Name:		perl-Email-LocalDelivery
Version:	0.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f59cc917a1b87189c5f1b0c3e4be9959
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{!?_without_tests:1}0
# the issue of different interpretation of version numbers between perl
# and rpm comes back again...  Here should be ">= 0.11", but the newest
# perl-Email-Foldertype is 0.5.
BuildRequires:	perl-Email-FolderType
BuildRequires:	perl-Email-Simple >= 1.4
BuildRequires:	perl-File-Path-Expand
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the second module produced by the "Perl Email Project", a
reaction against the complexity and increasing bugginess of the
Mail::* modules. It delivers an email to a list of mailboxes.

%description -l pl
To jest drugi modu³ wyprodukowany przez "Perl Email Project", bêd±cy
reakcj± na z³o¿ono¶æ i rosn±cy wspó³czynnik zapluskwienia modu³ów
Mail::*. Modu³ dostarcza pocztê do listy skrzynek.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
