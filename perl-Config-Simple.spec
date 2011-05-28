%define upstream_name    Config-Simple
%define upstream_version 4.59

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Config-Simple module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Config/Simple.pm
%{perl_vendorlib}/auto/Config/Simple
%{_mandir}/*/*
