%define upstream_name    Config-Simple
%define upstream_version 4.59

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Config-Simple module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Reading and writing configuration files is one of the most frequent
aspects of any software design. Config::Simple is the library to help
you with it.

Config::Simple is a class representing configuration file object. It
supports several configuration file syntax and tries to identify the
file syntax to parse them accordingly. Library supports parsing,
updating and creating configuration files.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}
find . -type f -exec chmod 0644 {} \;

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Config/Simple.pm
%{perl_vendorlib}/auto/Config/Simple
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 4.590.0-2mdv2011.0
+ Revision: 680843
- mass rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 4.590.0-1mdv2011.0
+ Revision: 406903
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 4.59-3mdv2009.0
+ Revision: 241190
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Jun 27 2007 Olivier Thauvin <nanardon@mandriva.org> 4.59-1mdv2008.0
+ Revision: 44827
- 4.59


* Mon Aug 28 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-08-28 14:49:52 (58413)
- mkrel
- check section

* Mon Aug 28 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-08-28 14:46:19 (58407)
Import perl-Config-Simple

* Wed Jul 20 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 4.58-1mdk
- 4.58

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 4.56-1mdk
- initial Mandriva package

