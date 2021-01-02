#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : mesa
Version  : 20.3.1
Release  : 256
URL      : https://gitlab.freedesktop.org/mesa/mesa/-/archive/mesa-20.3.1/mesa-mesa-20.3.1.tar.gz
Source0  : https://gitlab.freedesktop.org/mesa/mesa/-/archive/mesa-20.3.1/mesa-mesa-20.3.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: mesa-data = %{version}-%{release}
Requires: mesa-lib = %{version}-%{release}
BuildRequires : Mako-python
BuildRequires : Sphinx
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Loader-dev
BuildRequires : Vulkan-Tools
BuildRequires : Z3-dev
BuildRequires : Z3-staticdev
BuildRequires : binutils-dev
BuildRequires : bison
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-meson
BuildRequires : buildreq-scons
BuildRequires : doxygen
BuildRequires : elfutils-dev
BuildRequires : expat-dev
BuildRequires : flex
BuildRequires : gcc-dev
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : glibc-staticdev
BuildRequires : googletest-dev
BuildRequires : libclc-dev
BuildRequires : libedit
BuildRequires : libedit-dev
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libgcrypt-dev
BuildRequires : libpthread-stubs-dev
BuildRequires : libstdc++-dev
BuildRequires : libva-dev
BuildRequires : libvdpau-dev
BuildRequires : libxml2-staticdev
BuildRequires : llvm11
BuildRequires : llvm11-bin
BuildRequires : llvm11-data
BuildRequires : llvm11-dev
BuildRequires : llvm11-lib
BuildRequires : llvm11-libexec
BuildRequires : llvm11-staticdev
BuildRequires : ncurses-dev
BuildRequires : nettle-dev
BuildRequires : ninja
BuildRequires : pkgconfig(32libdrm_intel)
BuildRequires : pkgconfig(32xvmc)
BuildRequires : pkgconfig(dri3proto)
BuildRequires : pkgconfig(libdrm_intel)
BuildRequires : pkgconfig(libunwind)
BuildRequires : pkgconfig(presentproto)
BuildRequires : pkgconfig(valgrind)
BuildRequires : pkgconfig(xdamage)
BuildRequires : pkgconfig(xfixes)
BuildRequires : pkgconfig(xshmfence)
BuildRequires : pkgconfig(xvmc)
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : valgrind
BuildRequires : valgrind-dev
BuildRequires : wayland-dev
BuildRequires : wayland-protocols-dev
BuildRequires : xz-dev
BuildRequires : xz-staticdev
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
BuildRequires : zstd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: avx2-drivers.patch
Patch2: 0001-Revert-mesa-Enable-asm-unconditionally-now-that-gen_.patch
Patch3: 0001-Revert-egl-move-include-of-local-headers-out-of-Khro.patch

%description
A Vulkan layer to display information about the running application
using an overlay.

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


%package lib
Summary: lib components for the mesa package.
Group: Libraries
Requires: mesa-data = %{version}-%{release}

%description lib
lib components for the mesa package.


%prep
%setup -q -n mesa-mesa-20.3.1
cd %{_builddir}/mesa-mesa-20.3.1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1609554186
unset LD_AS_NEEDED
export GCC_IGNORE_WERROR=1
## altflags1 content
export CFLAGS="-O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
#
export CXXFLAGS="-O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC"
#
export FCFLAGS="-O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
export FFLAGS="-O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
export CFFLAGS="-O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
#
export LDFLAGS="-O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
#
unset CCACHE_DISABLE
export PATH="/usr/lib64/ccache/bin:$PATH"
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
## altflags1 end
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Ddefault_library=both -Dplatforms=x11,wayland \
-Ddri3=true \
-Ddri-drivers=i915,i965,nouveau,r100,r200 \
-Dgallium-drivers=radeonsi,r600,nouveau,svga,swrast,iris \
-Dcpp_std=gnu++14 \
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
-Dllvm=enabled \
-Dshared-llvm=disabled \
-Dselinux=false \
-Dosmesa=gallium \
-Dgallium-xvmc=true \
-Db_ndebug=true \
-Dprefer-iris=true  builddir
ninja -v -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install
## install_append content
#mv %{buildroot}/usr/lib64/haswell/dri/i965_dri.so %{buildroot}/usr/lib64/dri/i965_dri.so.avx2
#mv %{buildroot}/usr/lib64/haswell/dri/swrast_dri.so %{buildroot}/usr/lib64/dri/swrast_dri.so.avx2
#mv %{buildroot}/usr/lib64/haswell/dri/iris_dri.so %{buildroot}/usr/lib64/dri/iris_dri.so.avx2
#ln -s i965_dri.so %{buildroot}/usr/lib64/dri/i915_dri.so

#rm -rf  %{buildroot}/usr/lib64/haswell

#sed 's/lib64/lib32/' %{buildroot}/usr/share/vulkan/icd.d/intel_icd.x86_64.json > %{buildroot}/usr/share/vulkan/icd.d/intel_icd.i686.json
#sed 's/lib64/lib32/' %{buildroot}/usr/share/vulkan/icd.d/radeon_icd.x86_64.json > %{buildroot}/usr/share/vulkan/icd.d/radeon_icd.i686.json
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
/usr/include/EGL/egl.h
/usr/include/EGL/eglext.h
/usr/include/EGL/eglextchromium.h
/usr/include/EGL/eglmesaext.h
/usr/include/EGL/eglplatform.h
/usr/include/GL/gl.h
/usr/include/GL/glcorearb.h
/usr/include/GL/glext.h
/usr/include/GL/glx.h
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
/usr/include/gbm.h
/usr/include/vulkan/vulkan_intel.h
/usr/include/xa_composite.h
/usr/include/xa_context.h
/usr/include/xa_tracker.h
/usr/lib64/pkgconfig/dri.pc
/usr/lib64/pkgconfig/egl.pc
/usr/lib64/pkgconfig/gbm.pc
/usr/lib64/pkgconfig/gl.pc
/usr/lib64/pkgconfig/glesv1_cm.pc
/usr/lib64/pkgconfig/glesv2.pc
/usr/lib64/pkgconfig/osmesa.pc
/usr/lib64/pkgconfig/xatracker.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/dri/i915_dri.so
/usr/lib64/dri/i965_dri.so
/usr/lib64/dri/iris_dri.so
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
/usr/lib64/gallium-pipe/pipe_iris.so
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
/usr/lib64/libXvMCnouveau.so.1
/usr/lib64/libXvMCnouveau.so.1.0
/usr/lib64/libXvMCnouveau.so.1.0.0
/usr/lib64/libXvMCr600.so
/usr/lib64/libXvMCr600.so.1
/usr/lib64/libXvMCr600.so.1.0
/usr/lib64/libXvMCr600.so.1.0.0
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
