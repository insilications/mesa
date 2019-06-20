#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mesa
Version  : 19.0+4385.g10895c39c33
Release  : 214
URL      : https://gitlab.freedesktop.org/mesa/mesa/-/archive/10895c39c338d9e4a00c86590bdfd4e30bd2acfe/mesa-19.0+4385-g10895c39c33.tar.bz2
Source0  : https://gitlab.freedesktop.org/mesa/mesa/-/archive/10895c39c338d9e4a00c86590bdfd4e30bd2acfe/mesa-19.0+4385-g10895c39c33.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: mesa-data = %{version}-%{release}
Requires: mesa-lib = %{version}-%{release}
Requires: mesa-license = %{version}-%{release}
BuildRequires : Mako-python
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Loader-dev
BuildRequires : Vulkan-Loader-dev32
BuildRequires : Vulkan-Tools
BuildRequires : bison
BuildRequires : buildreq-meson
BuildRequires : buildreq-scons
BuildRequires : elfutils-dev32
BuildRequires : expat-dev
BuildRequires : expat-dev32
BuildRequires : flex
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libX11-dev32
BuildRequires : libXv-dev
BuildRequires : libXv-dev32
BuildRequires : libclc-dev
BuildRequires : libgcrypt-dev
BuildRequires : libpthread-stubs-dev
BuildRequires : libunwind-dev32
BuildRequires : libva-dev
BuildRequires : libvdpau-dev
BuildRequires : llvm-dev
BuildRequires : llvm-dev32
BuildRequires : nettle-dev
BuildRequires : nettle-dev32
BuildRequires : pkg-config
BuildRequires : pkgconfig(32dri3proto)
BuildRequires : pkgconfig(32libdrm_intel)
BuildRequires : pkgconfig(32xdamage)
BuildRequires : pkgconfig(32xext)
BuildRequires : pkgconfig(32xfixes)
BuildRequires : pkgconfig(32xrandr)
BuildRequires : pkgconfig(32xshmfence)
BuildRequires : pkgconfig(32xvmc)
BuildRequires : pkgconfig(32xxf86vm)
BuildRequires : pkgconfig(dri3proto)
BuildRequires : pkgconfig(libdrm_intel)
BuildRequires : pkgconfig(presentproto)
BuildRequires : pkgconfig(valgrind)
BuildRequires : pkgconfig(xdamage)
BuildRequires : pkgconfig(xfixes)
BuildRequires : pkgconfig(xrandr)
BuildRequires : pkgconfig(xshmfence)
BuildRequires : pkgconfig(xvmc)
BuildRequires : pkgconfig(xxf86vm)
BuildRequires : valgrind
BuildRequires : wayland-dev
BuildRequires : wayland-dev32
BuildRequires : wayland-protocols-dev
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
Patch1: avx2-drivers.patch
Patch2: 0001-Attempt-at-fixing-strict-aliasing-violation-in-deque.patch

%description
Dear ImGui
==========
This directory contains a copy of the Dear ImGui library
(https://github.com/ocornut/imgui) at the following commit :

%package data
Summary: data components for the mesa package.
Group: Data

%description data
data components for the mesa package.


%package dev
Summary: dev components for the mesa package.
Group: Development
Requires: mesa-lib = %{version}-%{release}
Requires: mesa-data = %{version}-%{release}
Provides: mesa-devel = %{version}-%{release}
Requires: mesa = %{version}-%{release}

%description dev
dev components for the mesa package.


%package dev32
Summary: dev32 components for the mesa package.
Group: Default
Requires: mesa-lib32 = %{version}-%{release}
Requires: mesa-data = %{version}-%{release}
Requires: mesa-dev = %{version}-%{release}

%description dev32
dev32 components for the mesa package.


%package lib
Summary: lib components for the mesa package.
Group: Libraries
Requires: mesa-data = %{version}-%{release}
Requires: mesa-license = %{version}-%{release}

%description lib
lib components for the mesa package.


%package lib32
Summary: lib32 components for the mesa package.
Group: Default
Requires: mesa-data = %{version}-%{release}
Requires: mesa-license = %{version}-%{release}

%description lib32
lib32 components for the mesa package.


%package license
Summary: license components for the mesa package.
Group: Default

%description license
license components for the mesa package.


%prep
%setup -q -n mesa-10895c39c338d9e4a00c86590bdfd4e30bd2acfe
%patch1 -p1
%patch2 -p1
pushd ..
cp -a mesa-10895c39c338d9e4a00c86590bdfd4e30bd2acfe build32
popd
pushd ..
cp -a mesa-10895c39c338d9e4a00c86590bdfd4e30bd2acfe buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1561063701
unset LD_AS_NEEDED
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain -Dplatforms=x11,drm,wayland,surfaceless \
-Ddri3=true \
-Ddri-drivers=i915,i965,nouveau,r100,r200 \
-Dgallium-drivers=radeonsi,r600,nouveau,svga,swrast \
-Dcpp_std=gnu++11 \
-Dgallium-va=true \
-Dgallium-xa=true \
-Dgallium-opencl=icd \
-Dvulkan-drivers=intel,amd \
-Dshared-glapi=true \
-Dgles2=true \
-Dgbm=true \
-Dopengl=true \
-Dglx=dri \
-Degl=true \
-Dglvnd=false \
-Dasm=true \
-Dosmesa=classic \
-Dllvm=true \
-Dshared-llvm=true \
-Dselinux=false \
-Dosmesa=gallium \
-Dgallium-xvmc=true \
-Db_ndebug=true  builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=haswell" CXXFLAGS="$CXXFLAGS -m64 -march=haswell " LDFLAGS="$LDFLAGS -m64 -march=haswell" meson --prefix /usr --libdir=/usr/lib64/haswell --buildtype=plain -Dplatforms=x11,drm,wayland,surfaceless \
-Ddri3=true \
-Ddri-drivers=i915,i965,nouveau,r100,r200 \
-Dgallium-drivers=radeonsi,r600,nouveau,svga,swrast \
-Dcpp_std=gnu++11 \
-Dgallium-va=true \
-Dgallium-xa=true \
-Dgallium-opencl=icd \
-Dvulkan-drivers=intel,amd \
-Dshared-glapi=true \
-Dgles2=true \
-Dgbm=true \
-Dopengl=true \
-Dglx=dri \
-Degl=true \
-Dglvnd=false \
-Dasm=true \
-Dosmesa=classic \
-Dllvm=true \
-Dshared-llvm=true \
-Dselinux=false \
-Dosmesa=gallium \
-Dgallium-xvmc=true \
-Db_ndebug=true  builddiravx2
ninja -v -C builddiravx2
pushd ../build32
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32"
meson --libdir=/usr/lib32 --prefix /usr --buildtype=plain -Dplatforms=x11,drm,wayland,surfaceless \
-Ddri3=true \
-Ddri-drivers=i915,i965,nouveau,r100,r200 \
-Dgallium-drivers=radeonsi,r600,nouveau,svga,swrast \
-Dcpp_std=gnu++11 \
-Dgallium-va=true \
-Dgallium-xa=true \
-Dgallium-opencl=icd \
-Dvulkan-drivers=intel,amd \
-Dshared-glapi=true \
-Dgles2=true \
-Dgbm=true \
-Dopengl=true \
-Dglx=dri \
-Degl=true \
-Dglvnd=false \
-Dasm=true \
-Dosmesa=classic \
-Dllvm=true \
-Dshared-llvm=true \
-Dselinux=false \
-Dosmesa=gallium \
-Dgallium-xvmc=true \
-Db_ndebug=true -Dasm=false \
-Dgallium-opencl=disabled builddir
ninja -v -C builddir
popd

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mesa
cp src/imgui/LICENSE.txt %{buildroot}/usr/share/package-licenses/mesa/src_imgui_LICENSE.txt
cp src/mapi/glapi/gen/license.py %{buildroot}/usr/share/package-licenses/mesa/src_mapi_glapi_gen_license.py
pushd ../build32
DESTDIR=%{buildroot} ninja -C builddir install
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
DESTDIR=%{buildroot} ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
## install_append content
mv %{buildroot}/usr/lib64/haswell/dri/i965_dri.so %{buildroot}/usr/lib64/dri/i965_dri.so.avx2
rm -rf  %{buildroot}/usr/lib64/haswell
## install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/drirc.d/00-mesa-defaults.conf
/usr/share/vulkan/icd.d/intel_icd.x86_64.json
/usr/share/vulkan/icd.d/radeon_icd.x86_64.json

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/EGL/egl.h
/usr/include/EGL/eglext.h
/usr/include/EGL/eglextchromium.h
/usr/include/EGL/eglmesaext.h
/usr/include/EGL/eglplatform.h
/usr/include/GL/gl.h
/usr/include/GL/gl_mangle.h
/usr/include/GL/glcorearb.h
/usr/include/GL/glext.h
/usr/include/GL/glx.h
/usr/include/GL/glx_mangle.h
/usr/include/GL/glxext.h
/usr/include/GL/internal/dri_interface.h
/usr/include/GL/osmesa.h
/usr/include/GLES/egl.h
/usr/include/GLES/gl.h
/usr/include/GLES/glext.h
/usr/include/GLES/glplatform.h
/usr/include/GLES2/gl2.h
/usr/include/GLES2/gl2ext.h
/usr/include/GLES2/gl2platform.h
/usr/include/GLES3/gl3.h
/usr/include/GLES3/gl31.h
/usr/include/GLES3/gl32.h
/usr/include/GLES3/gl3ext.h
/usr/include/GLES3/gl3platform.h
/usr/include/KHR/khrplatform.h
/usr/include/vulkan/vulkan_intel.h
/usr/lib64/pkgconfig/dri.pc
/usr/lib64/pkgconfig/egl.pc
/usr/lib64/pkgconfig/gbm.pc
/usr/lib64/pkgconfig/gl.pc
/usr/lib64/pkgconfig/glesv1_cm.pc
/usr/lib64/pkgconfig/glesv2.pc
/usr/lib64/pkgconfig/osmesa.pc
/usr/lib64/pkgconfig/xatracker.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/pkgconfig/32dri.pc
/usr/lib32/pkgconfig/32egl.pc
/usr/lib32/pkgconfig/32gbm.pc
/usr/lib32/pkgconfig/32gl.pc
/usr/lib32/pkgconfig/32glesv1_cm.pc
/usr/lib32/pkgconfig/32glesv2.pc
/usr/lib32/pkgconfig/32osmesa.pc
/usr/lib32/pkgconfig/32xatracker.pc
/usr/lib32/pkgconfig/dri.pc
/usr/lib32/pkgconfig/egl.pc
/usr/lib32/pkgconfig/gbm.pc
/usr/lib32/pkgconfig/gl.pc
/usr/lib32/pkgconfig/glesv1_cm.pc
/usr/lib32/pkgconfig/glesv2.pc
/usr/lib32/pkgconfig/osmesa.pc
/usr/lib32/pkgconfig/xatracker.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/dri/i915_dri.so
/usr/lib64/dri/i965_dri.so
/usr/lib64/dri/i965_dri.so.avx2
/usr/lib64/dri/kms_swrast_dri.so
/usr/lib64/dri/nouveau_dri.so
/usr/lib64/dri/nouveau_drv_video.so
/usr/lib64/dri/nouveau_vieux_dri.so
/usr/lib64/dri/r200_dri.so
/usr/lib64/dri/r600_dri.so
/usr/lib64/dri/r600_drv_video.so
/usr/lib64/dri/radeon_dri.so
/usr/lib64/dri/radeonsi_dri.so
/usr/lib64/dri/radeonsi_drv_video.so
/usr/lib64/dri/swrast_dri.so
/usr/lib64/dri/vmwgfx_dri.so
/usr/lib64/gallium-pipe/pipe_nouveau.so
/usr/lib64/gallium-pipe/pipe_r600.so
/usr/lib64/gallium-pipe/pipe_radeonsi.so
/usr/lib64/gallium-pipe/pipe_swrast.so
/usr/lib64/gallium-pipe/pipe_vmwgfx.so
/usr/lib64/libEGL.so
/usr/lib64/libEGL.so.1
/usr/lib64/libEGL.so.1.0.0
/usr/lib64/libGL.so
/usr/lib64/libGL.so.1
/usr/lib64/libGL.so.1.2.0
/usr/lib64/libGLESv1_CM.so
/usr/lib64/libGLESv1_CM.so.1
/usr/lib64/libGLESv1_CM.so.1.1.0
/usr/lib64/libGLESv2.so
/usr/lib64/libGLESv2.so.2
/usr/lib64/libGLESv2.so.2.0.0
/usr/lib64/libMesaOpenCL.so
/usr/lib64/libMesaOpenCL.so.1
/usr/lib64/libMesaOpenCL.so.1.0.0
/usr/lib64/libOSMesa.so
/usr/lib64/libOSMesa.so.8
/usr/lib64/libOSMesa.so.8.0.0
/usr/lib64/libXvMCnouveau.so
/usr/lib64/libXvMCr600.so
/usr/lib64/libgbm.so
/usr/lib64/libgbm.so.1
/usr/lib64/libgbm.so.1.0.0
/usr/lib64/libglapi.so
/usr/lib64/libglapi.so.0
/usr/lib64/libglapi.so.0.0.0
/usr/lib64/libvulkan_intel.so
/usr/lib64/libvulkan_radeon.so
/usr/lib64/libxatracker.so
/usr/lib64/libxatracker.so.2
/usr/lib64/libxatracker.so.2.5.0
/usr/lib64/vdpau/libvdpau_nouveau.so
/usr/lib64/vdpau/libvdpau_nouveau.so.1
/usr/lib64/vdpau/libvdpau_nouveau.so.1.0
/usr/lib64/vdpau/libvdpau_nouveau.so.1.0.0
/usr/lib64/vdpau/libvdpau_r600.so
/usr/lib64/vdpau/libvdpau_r600.so.1
/usr/lib64/vdpau/libvdpau_r600.so.1.0
/usr/lib64/vdpau/libvdpau_r600.so.1.0.0
/usr/lib64/vdpau/libvdpau_radeonsi.so
/usr/lib64/vdpau/libvdpau_radeonsi.so.1
/usr/lib64/vdpau/libvdpau_radeonsi.so.1.0
/usr/lib64/vdpau/libvdpau_radeonsi.so.1.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/dri/i915_dri.so
/usr/lib32/dri/i965_dri.so
/usr/lib32/dri/kms_swrast_dri.so
/usr/lib32/dri/nouveau_dri.so
/usr/lib32/dri/nouveau_drv_video.so
/usr/lib32/dri/nouveau_vieux_dri.so
/usr/lib32/dri/r200_dri.so
/usr/lib32/dri/r600_dri.so
/usr/lib32/dri/r600_drv_video.so
/usr/lib32/dri/radeon_dri.so
/usr/lib32/dri/radeonsi_dri.so
/usr/lib32/dri/radeonsi_drv_video.so
/usr/lib32/dri/swrast_dri.so
/usr/lib32/dri/vmwgfx_dri.so
/usr/lib32/libEGL.so
/usr/lib32/libEGL.so.1
/usr/lib32/libEGL.so.1.0.0
/usr/lib32/libGL.so
/usr/lib32/libGL.so.1
/usr/lib32/libGL.so.1.2.0
/usr/lib32/libGLESv1_CM.so
/usr/lib32/libGLESv1_CM.so.1
/usr/lib32/libGLESv1_CM.so.1.1.0
/usr/lib32/libGLESv2.so
/usr/lib32/libGLESv2.so.2
/usr/lib32/libGLESv2.so.2.0.0
/usr/lib32/libOSMesa.so
/usr/lib32/libOSMesa.so.8
/usr/lib32/libOSMesa.so.8.0.0
/usr/lib32/libXvMCnouveau.so
/usr/lib32/libXvMCr600.so
/usr/lib32/libgbm.so
/usr/lib32/libgbm.so.1
/usr/lib32/libgbm.so.1.0.0
/usr/lib32/libglapi.so
/usr/lib32/libglapi.so.0
/usr/lib32/libglapi.so.0.0.0
/usr/lib32/libvulkan_intel.so
/usr/lib32/libvulkan_radeon.so
/usr/lib32/libxatracker.so
/usr/lib32/libxatracker.so.2
/usr/lib32/libxatracker.so.2.5.0
/usr/lib32/vdpau/libvdpau_nouveau.so
/usr/lib32/vdpau/libvdpau_nouveau.so.1
/usr/lib32/vdpau/libvdpau_nouveau.so.1.0
/usr/lib32/vdpau/libvdpau_nouveau.so.1.0.0
/usr/lib32/vdpau/libvdpau_r600.so
/usr/lib32/vdpau/libvdpau_r600.so.1
/usr/lib32/vdpau/libvdpau_r600.so.1.0
/usr/lib32/vdpau/libvdpau_r600.so.1.0.0
/usr/lib32/vdpau/libvdpau_radeonsi.so
/usr/lib32/vdpau/libvdpau_radeonsi.so.1
/usr/lib32/vdpau/libvdpau_radeonsi.so.1.0
/usr/lib32/vdpau/libvdpau_radeonsi.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mesa/src_imgui_LICENSE.txt
/usr/share/package-licenses/mesa/src_mapi_glapi_gen_license.py
