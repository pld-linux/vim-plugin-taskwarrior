%define		plugin		taskwarrior
%define		rev		8ae6c5e
%define		timestamp	20210107
Summary:	Vim plugin: vim interface for taskwarrior
Name:		vim-plugin-%{plugin}
Version:	1.0
Release:	0.%{timestamp}.1
License:	MIT
Group:		Applications/Editors/Vim
Source0:	https://codeload.github.com/blindFS/vim-taskwarrior/tar.gz/%{rev}?/%{name}-%{version}-%{rev}.tar.gz
# Source0-md5:	c78893021c5ec4be43772d9b98e0f5bd
URL:		https://github.com/blindFS/vim-taskwarrior
Requires:	taskwarrior >= 2.3
Requires:	vim-plugin-webapi
Requires:	vim-rt >= 4:7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim

%description
vim-taskwarrior is a vim plugin that extends taskwarrior with an
interactive interface. It features a rich set of mappings and
commands, is easy to customize, and makes adding, modifying, sorting,
reporting and marking done, fast, easy and fun!

%package doc
Summary:	Documentation for taskwarrior Vim plugin
Requires(post,postun):	/usr/bin/vim
Requires:	%{name} = %{version}-%{release}
Requires:	vim-rt >= 4:7.4.2054-2

%description doc
Documentation for taskwarrior Vim plugin.

%package -n vim-plugin-airline-extension-taskwarrior
Summary:	Airline plugin extension with support for taskwarrior
Requires:	%{name} = %{version}-%{release}
Requires:	vim-plugin-airline
Requires:	vim-plugin-taskwarrior

%description -n vim-plugin-airline-extension-taskwarrior
Airline plugin extension with support for taskwarrior.

%prep
%setup -qn vim-taskwarrior-%{rev}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}
cp -pr autoload doc ftplugin plugin syntax $RPM_BUILD_ROOT%{_vimdatadir}

%{__rm} -r $RPM_BUILD_ROOT%{_vimdatadir}/autoload/webapi

%clean
rm -rf $RPM_BUILD_ROOT

%post doc
%vim_doc_helptags

%postun doc
%vim_doc_helptags

%files
%defattr(644,root,root,755)
%doc README.md
%{_vimdatadir}/autoload/taskwarrior
%{_vimdatadir}/autoload/taskwarrior.vim
%{_vimdatadir}/autoload/taskinfo.vim
%{_vimdatadir}/ftplugin/taskreport.vim
%{_vimdatadir}/plugin/taskwarrior.vim
%{_vimdatadir}/syntax/taskinfo.vim
%{_vimdatadir}/syntax/taskreport.vim

%files doc
%defattr(644,root,root,755)
%{_vimdatadir}/doc/vim-tw.txt

%files -n vim-plugin-airline-extension-taskwarrior
%defattr(644,root,root,755)
%{_vimdatadir}/autoload/airline/extensions/taskwarrior.vim
