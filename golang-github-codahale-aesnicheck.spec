# https://github.com/codahale/aesnicheck
%global goipath         github.com/codahale/aesnicheck
%global commit          349fcc471aaccc29cd074e1275f1a494323826cd

%global common_description %{expand:
A Go library for checking AES-NI support.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        A Go library for checking AES-NI support
# Detected licences
# - Expat License at 'LICENSE'
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Wed Nov 14 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20181114git349fcc4
- Bump to commit 349fcc471aaccc29cd074e1275f1a494323826cd
- Update to new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20140702git349fcc4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20140702git349fcc4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 06 2017 Clément David <c.david86@gmail.com> - 0-0.1.20140702git349fcc4
- Initial package for Fedora

