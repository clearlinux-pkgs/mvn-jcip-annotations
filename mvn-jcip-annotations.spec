#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-jcip-annotations
Version  : 1.0.1
Release  : 3
URL      : https://github.com/stephenc/jcip-annotations/archive/jcip-annotations-1.0-1.tar.gz
Source0  : https://github.com/stephenc/jcip-annotations/archive/jcip-annotations-1.0-1.tar.gz
Source1  : https://repo1.maven.org/maven2/com/github/stephenc/jcip/jcip-annotations/1.0-1/jcip-annotations-1.0-1.jar
Source2  : https://repo1.maven.org/maven2/com/github/stephenc/jcip/jcip-annotations/1.0-1/jcip-annotations-1.0-1.pom
Source3  : https://repo1.maven.org/maven2/net/jcip/jcip-annotations/1.0/jcip-annotations-1.0.jar
Source4  : https://repo1.maven.org/maven2/net/jcip/jcip-annotations/1.0/jcip-annotations-1.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-jcip-annotations-data = %{version}-%{release}

%description
<!---
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

%package data
Summary: data components for the mvn-jcip-annotations package.
Group: Data

%description data
data components for the mvn-jcip-annotations package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/github/stephenc/jcip/jcip-annotations/1.0-1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/github/stephenc/jcip/jcip-annotations/1.0-1/jcip-annotations-1.0-1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/github/stephenc/jcip/jcip-annotations/1.0-1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/github/stephenc/jcip/jcip-annotations/1.0-1/jcip-annotations-1.0-1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/jcip/jcip-annotations/1.0
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/net/jcip/jcip-annotations/1.0/jcip-annotations-1.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/jcip/jcip-annotations/1.0
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/net/jcip/jcip-annotations/1.0/jcip-annotations-1.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/github/stephenc/jcip/jcip-annotations/1.0-1/jcip-annotations-1.0-1.jar
/usr/share/java/.m2/repository/com/github/stephenc/jcip/jcip-annotations/1.0-1/jcip-annotations-1.0-1.pom
/usr/share/java/.m2/repository/net/jcip/jcip-annotations/1.0/jcip-annotations-1.0.jar
/usr/share/java/.m2/repository/net/jcip/jcip-annotations/1.0/jcip-annotations-1.0.pom
