Name:           ros-jade-stereo-image-proc
Version:        1.12.18
Release:        0%{?dist}
Summary:        ROS stereo_image_proc package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/stereo_image_proc
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-cv-bridge
Requires:       ros-jade-dynamic-reconfigure
Requires:       ros-jade-image-geometry
Requires:       ros-jade-image-proc
Requires:       ros-jade-image-transport
Requires:       ros-jade-message-filters
Requires:       ros-jade-nodelet
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-stereo-msgs
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cv-bridge
BuildRequires:  ros-jade-dynamic-reconfigure
BuildRequires:  ros-jade-image-geometry
BuildRequires:  ros-jade-image-proc
BuildRequires:  ros-jade-image-transport
BuildRequires:  ros-jade-message-filters
BuildRequires:  ros-jade-nodelet
BuildRequires:  ros-jade-rostest
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-stereo-msgs

%description
Stereo and single image rectification and disparity processing.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Tue Jul 12 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.18-0
- Autogenerated by Bloom

* Mon Jul 11 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.17-0
- Autogenerated by Bloom

* Sat Mar 19 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.16-0
- Autogenerated by Bloom

* Sun Jan 17 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.15-0
- Autogenerated by Bloom

* Wed Jul 22 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.14-0
- Autogenerated by Bloom

* Wed Jan 14 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.12-0
- Autogenerated by Bloom

