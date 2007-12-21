%define real_name Config-Simple

Summary:	Config-Simple module for perl 
Name:		perl-%{real_name}
Version:	4.59
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Reading and writing configuration files is one of the most frequent
aspects of any software design. Config::Simple is the library to help
you with it.

Config::Simple is a class representing configuration file object. It
supports several configuration file syntax and tries to identify the
file syntax to parse them accordingly. Library supports parsing,
updating and creating configuration files.


%prep
%setup -q -n %{real_name}-%{version} 
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

