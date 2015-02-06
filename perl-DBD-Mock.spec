%define upstream_name    DBD-Mock
%define upstream_version 1.45
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.45
Release:	3

Summary:	Mock database driver for testing
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DBD/DBD-Mock-1.45.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DBI)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/DBD

%changelog
* Fri Jun 24 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.410.0-1mdv2011.0
+ Revision: 686989
- update to new version 1.41

* Wed Jun 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.400.0-1
+ Revision: 686628
- update to new version 1.40

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 1.390.0-2
+ Revision: 681352
- mass rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.390.0-1mdv2011.0
+ Revision: 403092
- rebuild using %%perl_convert_version

* Wed Nov 26 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.39-1mdv2009.1
+ Revision: 307032
- import perl-DBD-Mock


* Wed Nov 26 2008 cpan2dist 1.39-1mdv
- initial mdv release, generated with cpan2dist


