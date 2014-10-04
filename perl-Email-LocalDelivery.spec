#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Email
%define		pnam	LocalDelivery
Summary:	Email::LocalDelivery - deliver a piece of email - simply
Summary(pl.UTF-8):	Email::LocalDelivery - po prostu dostarczanie poczty
Name:		perl-Email-LocalDelivery
Version:	1.200
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Email/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6218c960f8f426b5c20a64b3fb7a6bf4
URL:		http://search.cpan.org/dist/Email-LocalDelivery/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
# the issue of different interpretation of version numbers between perl
# and rpm comes back again...  Here should be ">= 0.11", but the newest
# perl-Email-Foldertype is 0.5.
BuildRequires:	perl-Email-FolderType
BuildRequires:	perl-Email-Simple >= 1:1.998
BuildRequires:	perl-File-Path-Expand
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the second module produced by the "Perl Email Project", a
reaction against the complexity and increasing bugginess of the
Mail::* modules. It delivers an email to a list of mailboxes.

%description -l pl.UTF-8
To jest drugi moduł wyprodukowany przez "Perl Email Project", będący
reakcją na złożoność i rosnący współczynnik zapluskwienia modułów
Mail::*. Moduł dostarcza pocztę do listy skrzynek.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

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
