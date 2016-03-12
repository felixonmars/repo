# bcloud.spec
# Used to build rpm for bcloud on Fedora 21/22/23/rawhide
# Released by mosquito <sensor.wen@gmail.com>, wangjiezhe <wangjiezhe@gmail.com>
# This spec file is published under the GPLv3 license

# Template is originally generated by "rpmdev-newspec -t python"
%global debug_package %{nil}
%{!?python3_sitelib: %global python3_sitelib %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%global project bcloud
%global repo %{project}

# commit
%global _commit 4b54e0fdccf2b3013285fef05c97354cfa31697b
%global _shortcommit %(c=%{_commit}; echo ${c:0:7})

Name:    bcloud
Version: 3.8.2
Release: 3.git%{_shortcommit}%{?dist}
Summary: Baidu Pan client for Linux Desktop users
Summary(zh_CN): 百度网盘 Linux 桌面客户端

# https://raw.githubusercontent.com/LiuLang/bcloud/master/LICENSE
License: GPLv3
URL:     https://github.com/LiuLang/bcloud
Source0: https://github.com/LiuLang/bcloud/archive/%{_commit}/%{repo}-%{_shortcommit}.tar.gz

BuildArch: noarch
BuildRequires: python3-devel
Requires: gnome-icon-theme-symbolic
Requires: gtk3
Requires: libnotify
Requires: python3-crypto
Requires: python3-cssselect
Requires: python3-dbus
Requires: python3-gobject
Requires: python3-keyring
Requires: python3-lxml
Requires: python3-inotify
Recommends: libgnome-keyring, gnome-keyring
Recommends: python3-pykde4

%description
Baidu Pan client for Linux Desktop users.

%description -l zh_CN
百度网盘 Linux 桌面客户端.

%prep
%setup -q -n %repo-%{_commit}
# not bind cellphone
# https://github.com/LiuLang/bcloud/pull/177
sed -i '/err.*18/s|=.*18|in (18, 400032)|' bcloud/auth.py

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install \
    -O1 \
    --skip-build \
    --prefix=%{_prefix} \
    --root=%{buildroot}

%find_lang %{name}

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null ||:
/usr/bin/update-desktop-database -q ||:

%postun
if [ $1 -eq 0 ]; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null ||:
    /usr/bin/gtk-update-icon-cache -f -t -q %{_datadir}/icons/hicolor ||:
fi
/usr/bin/update-desktop-database -q ||:

%posttrans
/usr/bin/gtk-update-icon-cache -f -t -q %{_datadir}/icons/hicolor ||:

%files -f %{name}.lang
%doc README.md HISTORY
%license LICENSE
%{python3_sitelib}/*
%{_bindir}/%{name}-gui
%{_datadir}/icons/*
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop

%changelog
* Sat Mar 12 2016 mosquito <sensor.wen@gmail.com> - 3.8.2-3.git4b54e0f
- Add requires libgnome-keyring, python3-pykde4

* Sat Feb  6 2016 mosquito <sensor.wen@gmail.com> - 3.8.2-2.git4b54e0f
- Not bind cellphone

* Sun Jan 17 2016 mosquito <sensor.wen@gmail.com> - 3.8.2-1.git4b54e0f
- Update version to 3.8.2-1.git4b54e0f

* Sun Dec 20 2015 mosquito <sensor.wen@gmail.com> - 3.8.1-3.git75fab30
- Fix get bdstoken https://github.com/LiuLang/bcloud/pull/214

* Sat Dec 12 2015 mosquito <sensor.wen@gmail.com> - 3.8.1-2.git75fab30
- Update post script

* Thu Oct 22 2015 mosquito <sensor.wen@gmail.com> - 3.8.1-1.git75fab30
- Update version to 3.8.1-1.git75fab30
- Adjustment dependent

* Thu Sep 24 2015 mosquito <sensor.wen@gmail.com> - 3.7.2-2.git75fab30
- Update version to 3.7.2-2.git75fab30

* Mon Jul 13 2015 mosquito <sensor.wen@gmail.com> - 3.7.2-1.git40d8d2d
- Update version to 3.7.2-1.git40d8d2d

* Tue May 19 2015 mosquito <sensor.wen@gmail.com> - 3.7.1-1.git32abfb9
- Update version to 3.7.1-1.git32abfb9
- Update post script

* Wed May 06 2015 mosquito <sensor.wen@gmail.com> - 3.6.1-1.gitcffb757
- Rename version name

* Tue Feb 03 2015 mosquito <sensor.wen@gmail.com> - 3.6.1git20150201-1
- Update version to 3.6.1git20150201

* Sun Jan 18 2015 mosquito <sensor.wen@gmail.com> - 3.6.1git20150118-1
- Update version to 3.6.1git20150118

* Thu Jan 15 2015 mosquito <sensor.wen@gmail.com> - 3.6.1git20150113-1
- Update version to 3.6.1git20150113

* Mon Jan 12 2015 mosquito <sensor.wen@gmail.com> - 3.6.1git20150110-1
- Update version to 3.6.1git20150110

* Wed Jan 07 2015 mosquito <sensor.wen@gmail.com> - 3.5.10git20150106-1
- Update version to 3.5.10git20150106

* Wed Dec 31 2014 mosquito <sensor.wen@gmail.com> - 3.5.10git20141231-1
- Update version to 3.5.10git20141231

* Sun Dec 07 2014 mosquito <sensor.wen@gmail.com> - 3.5.10git20141206-1
- Update version to 3.5.10git20141206

* Sat Nov 29 2014 mosquito <sensor.wen@gmail.com> - 3.5.9git20141128-1
- Update version to 3.5.9git20141128

* Fri Nov 28 2014 mosquito <sensor.wen@gmail.com> - 3.5.9git20141127-1
- Update version to 3.5.9git20141127

* Thu Nov 27 2014 mosquito <sensor.wen@gmail.com> - 3.5.9git20141126-1
- Update version to 3.5.9git20141126

* Wed Nov 19 2014 mosquito <sensor.wen@gmail.com> - 3.5.8git20141119-1
- Update version to 3.5.8git20141119

* Mon Nov 17 2014 mosquito <sensor.wen@gmail.com> - 3.5.8git20141116-1
- Update version to 3.5.8git20141116

* Sun Nov 16 2014 mosquito <sensor.wen@gmail.com> - 3.5.8git20141115-1
- Update version to 3.5.8git20141115

* Tue Nov 11 2014 mosquito <sensor.wen@gmail.com> - 3.5.8git20141111-1
- Update version to 3.5.8git20141111

* Mon Nov 10 2014 mosquito <sensor.wen@gmail.com> - 3.5.8git20141110-1
- Update version to 3.5.8git20141110

* Fri Nov 7 2014 mosquito <sensor.wen@gmail.com> - 3.5.8git20141107-1
- Update version to 3.5.8git20141107

* Tue Nov 4 2014 mosquito <sensor.wen@gmail.com> - 3.5.7git20141103-1
- Update version to 3.5.7git20141103

* Thu Oct 30 2014 mosquito <sensor.wen@gmail.com> - 3.5.6git20141029-1
- Update version to 3.5.6git20141029
- Feature:
  * Feature: add navigation button to path box; https://github.com/LiuLang/bcloud/pull/74, https://github.com/LiuLang/bcloud/pull/80
  * Feature: support drag and drop in IconWindow
  * Feature: save view mode in IconWindow
  * Feature: show avatar
- Fixed:
  * Fixed: show default app_info in popup menu
  * Fixed: failed to load bcloud/bcloud.png; https://github.com/LiuLang/bcloud/pull/78
  * Fixed: TypeError: unknown type(null) in DownloadPage
  * i18n updated

* Sun Oct 19 2014 mosquito <sensor.wen@gmail.com> - 3.5.5git20141019-1
- Update version to 3.5.5git20141019
- Fixed:
  * Change url request timeout from 30s to 50s
  * Change log level from DEBUG to INFO
  * Set max downlaod retries to 10
  * Set max segments of download to 10
  * Update icons in IconView in order
  * Set connection timeout to 60s by default
  * Fixed: TypeError: Argument 1 does not allow None as a value
  * Remvoe test code

* Sun Oct 12 2014 mosquito <sensor.wen@gmail.com> - 3.5.4git20141012-2
- Rebuild

* Sun Oct 12 2014 mosquito <sensor.wen@gmail.com> - 3.5.4git20141012-1
- Update version to 3.5.4git20141012
- Fixed:
  * 'CloudPage' object has not attribute 'on_remove_button_clicked'
  * 'App' object has no attribute 'home_page'
  * failed to check file downloaded signal
  * check task exists in task list
  * catch truncate() exception
  * emit network-error signal when socket timed out
  * type object 'State' has no attribute 'UPLOADING'; reported by @yui133107
  * 'NoneType' object has no attribute 'value'
- Feature:
  * use new UI style in gtk-3.12
  * Signin Dialog redesigned
  * replace WAP API with passport API
  * use single thread when downloading small files
- Update:
  * Add log module
  * Simplify download speed calculation
  * Redesign download speed label
  * Support Linut Mint 17
  * Not work with Ubuntu 12.04 any more
  * Using PKCS1_v1_5 as RSA encrypt method
  * i18n updated

* Sat Oct 11 2014 mosquito <sensor.wen@gmail.com> - 3.5.3git20141007-1
- Initial build
- Fixed:
  * modify file handler mode from `ab` to `rb+`. That's a serious problem!
  * average download speed is incorrect; see https://github.com/LiuLang/bcloud/issues/15
