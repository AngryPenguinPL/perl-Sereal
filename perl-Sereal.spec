%define upstream_name Sereal
%define upstream_version 4.005

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %upstream_version
Release:        1
Summary:        Fast, compact, powerful binary (de-)serialization
# Makefile.PL defines LICENSE
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{upstream_name}/
Source0:        http://www.cpan.org/authors/id/Y/YV/YVES/%{upstream_name}-%{upstream_version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl
# blib not used
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
# Devel::CheckLib not used
BuildRequires:  perl(ExtUtils::MakeMaker)
# File::Find not used
# File::Path not used
# File::Spec not used
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Sereal::Decoder) >= 3.14
BuildRequires:  perl(Sereal::Encoder) >= 3.14
# Tests:
# Benchmark not used
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(integer)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sereal::Decoder::Constants)
BuildRequires:  perl(Sereal::Encoder::Constants)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::LongString)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::Scalar)
# Time::HiRes not used
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
# Optional tests:
BuildRequires:  perl(Test::Deep) >= 0.110
BuildRequires:  perl(Test::Deep::NoTest)

%description
Sereal is an efficient, compact-output, binary and feature-rich serialization
protocol. The Perl encoder is implemented as the Sereal::Encoder module, the
Perl decoder correspondingly as Sereal::Decoder. This Sereal module is a very
thin wrapper around both Sereal::Encoder and Sereal::Decoder. It depends on
both and loads both.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

find %{buildroot} -name '*.packlist' -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*
