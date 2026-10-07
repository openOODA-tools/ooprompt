Name:           ooprompt
Version:        0.1.0
Release:        1%{?dist}
Summary:        Reactive multi-segment shell prompt rendering git posture, capability level, and latency.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooprompt
Source0:        ooprompt-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooprompt is a sovereign, capability-bounded STATUS DISPLAY written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooprompt
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooprompt-uninstall

%files
/usr/bin/ooprompt
/usr/bin/ooprompt-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
