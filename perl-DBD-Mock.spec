%define upstream_name    DBD-Mock
%define upstream_version 1.39

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Mock database driver for testing
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/DBD/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(DBI)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Testing with databases can be tricky. If you are developing a system
married to a single database then you can make some assumptions about your
environment and ask the user to provide relevant connection information.
But if you need to test a framework that uses DBI, particularly a framework
that uses different types of persistence schemes, then it may be more
useful to simply verify what the framework is trying to do -- ensure the
right SQL is generated and that the correct parameters are bound.
'DBD::Mock' makes it easy to just modify your configuration (presumably
held outside your code) and just use it instead of 'DBD::Foo' (like the
DBD::Pg manpage or the DBD::mysql manpage) in your framework.

There is no distinct area where using this module makes sense. (Some people
may successfully argue that this is a solution looking for a problem...)
Indeed, if you can assume your users have something like the DBD::AnyData
manpage or the DBD::SQLite manpage or if you do not mind creating a
dependency on them then it makes far more sense to use these legitimate
driver implementations and test your application in the real world -- at
least as much of the real world as you can create in your tests...

And if your database handle exists as a package variable or something else
easily replaced at test-time then it may make more sense to use the
Test::MockObject manpage to create a fully dynamic handle. There is an
excellent article by chromatic about using the Test::MockObject manpage in
this and other ways, strongly recommended. (See the SEE ALSO manpage for a
link)

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/DBD
