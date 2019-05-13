Name:		postgres-decoderbufs
Version:	0.9.5
Release:	1%{?dist}
Summary:	PostgreSQL Protocol Buffers logical decoder plugin

License:	MIT
URL:		https://github.com/debezium/postgres-decoderbufs

%global full_version %{version}.Final

Source0:	https://github.com/debezium/%{name}/archive/v%{full_version}.tar.gz

BuildRequires:	gcc
BuildRequires:	postgresql-devel >= 11, postgresql-server-devel >= 11, postgresql-devel < 12, postgresql-server-devel < 12, postgis-devel < 12
BuildRequires:	postgis-devel >= 2
BuildRequires:	protobuf-c-devel

Requires:	protobuf-c
%{?postgresql_module_requires}

Recommends:	postgis

%description
A PostgreSQL logical decoder output plugin to deliver data as Protocol Buffers messages.

%prep
%setup -qn postgres-decoderbufs-%{full_version}


%build
%make_build


%install
%make_install


%files
%doc README.md
%license LICENSE
%{_libdir}/pgsql/decoderbufs.so
%{_datadir}/pgsql/extension/decoderbufs.control


%changelog
* Tue May 14 2019 - Jiri Pechanec <jpechane@redhat.com> 0.9.5-1
- Initial RPM packaging
