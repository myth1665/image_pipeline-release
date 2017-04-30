Name:           ros-lunar-image-view
Version:        1.12.20
Release:        0%{?dist}
Summary:        ROS image_view package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/image_view
Source0:        %{name}-%{version}.tar.gz

Requires:       gtk2-devel
Requires:       ros-lunar-camera-calibration-parsers
Requires:       ros-lunar-cv-bridge >= 1.11.13
Requires:       ros-lunar-dynamic-reconfigure
Requires:       ros-lunar-image-transport
Requires:       ros-lunar-message-filters
Requires:       ros-lunar-nodelet
Requires:       ros-lunar-rosconsole
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-std-srvs
BuildRequires:  gtk2-devel
BuildRequires:  ros-lunar-camera-calibration-parsers
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-cv-bridge >= 1.11.13
BuildRequires:  ros-lunar-dynamic-reconfigure
BuildRequires:  ros-lunar-image-transport
BuildRequires:  ros-lunar-message-filters
BuildRequires:  ros-lunar-message-generation
BuildRequires:  ros-lunar-nodelet
BuildRequires:  ros-lunar-rosconsole
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-rostest
BuildRequires:  ros-lunar-sensor-msgs
BuildRequires:  ros-lunar-std-srvs
BuildRequires:  ros-lunar-stereo-msgs

%description
A simple viewer for ROS image topics. Includes a specialized viewer for stereo +
disparity images.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Sun Apr 30 2017 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.20-0
- Autogenerated by Bloom

* Fri Apr 21 2017 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.19-0
- Autogenerated by Bloom

