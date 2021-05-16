#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : llvm_32
Version  : 12.0.1
Release  : 131
URL      : file:///insilications/apps/llvm-12.0.1.tar.gz
Source0  : file:///insilications/apps/llvm-12.0.1.tar.gz
Summary  : Google microbenchmark framework
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0
BuildRequires : PyYAML
BuildRequires : Pygments
BuildRequires : Sphinx
BuildRequires : Vulkan-Headers-dev Vulkan-Loader-dev Vulkan-Tools
BuildRequires : Z3-dev
BuildRequires : Z3-dev32
BuildRequires : Z3-staticdev
BuildRequires : binutils-dev
BuildRequires : binutils-extras
BuildRequires : bison
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-golang
BuildRequires : cmake
BuildRequires : dejagnu
BuildRequires : docbook-utils
BuildRequires : docbook-xml
BuildRequires : doxygen
BuildRequires : elfutils-dev
BuildRequires : expect
BuildRequires : flex
BuildRequires : gcc
BuildRequires : gcc-abi
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-doc
BuildRequires : gcc-go
BuildRequires : gcc-go-lib
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : gdb-dev
BuildRequires : git
BuildRequires : glibc-bin
BuildRequires : glibc-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-doc
BuildRequires : glibc-extras
BuildRequires : glibc-lib-avx2
BuildRequires : glibc-libc32
BuildRequires : glibc-locale
BuildRequires : glibc-nscd
BuildRequires : glibc-staticdev
BuildRequires : glibc-utils
BuildRequires : gmp-dev
BuildRequires : googletest-dev
BuildRequires : graphviz
BuildRequires : grep
BuildRequires : guile
BuildRequires : libedit
BuildRequires : libedit-dev
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libgcc1
BuildRequires : libstdc++
BuildRequires : libunwind-dev
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : libxslt
BuildRequires : lua-dev
BuildRequires : mpc-dev
BuildRequires : mpfr-dev
BuildRequires : ncurses
BuildRequires : ncurses-abi
BuildRequires : ncurses-bin
BuildRequires : ncurses-data
BuildRequires : ncurses-dev
BuildRequires : ncurses-dev32
BuildRequires : ncurses-lib
BuildRequires : ncurses-lib-narrow
BuildRequires : ncurses-lib-plusplus
BuildRequires : ncurses-lib32
BuildRequires : ninja
BuildRequires : perl
BuildRequires : pkg-config
BuildRequires : pkgconfig(32libffi)
BuildRequires : pkgconfig(libedit)
BuildRequires : pkgconfig(libffi)
BuildRequires : pkgconfig(zlib)
BuildRequires : procps-ng
BuildRequires : protobuf-dev
BuildRequires : ptyprocess
BuildRequires : pybind11-python3
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : sed
BuildRequires : swig
BuildRequires : tcl
BuildRequires : texinfo
BuildRequires : util-linux
BuildRequires : valgrind-dev
BuildRequires : xz-dev
BuildRequires : xz-dev32
BuildRequires : xz-staticdev
BuildRequires : xz-staticdev32
BuildRequires : yaml
BuildRequires : yaml-cpp
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
BuildRequires : zlib-staticdev
BuildRequires : zlib-staticdev32
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-llvm-Improve-physical-core-count-detection.patch
Patch2: 0002-llvm-Allow-one-more-FMA-fusion.patch
Patch3: 0004-llvm-Add-the-LLVM-major-version-number-to-the-Gold-L.patch
Patch4: 0005-llvm-Add-a-couple-more-f-instructions-that-GCC-has-t.patch

%description
Polly - Polyhedral optimizations for LLVM
-----------------------------------------
http://polly.llvm.org/

%prep
%setup -q -n llvm-12.0.1
cd %{_builddir}/llvm-12.0.1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1621164519
unset LD_AS_NEEDED
mkdir -p clr-build32
pushd clr-build32
## altflags1_32 content
unset LD_LIBRARY_PATH
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CCACHE_DISABLE=true
export V=1
export VERBOSE=1
export PATH="/usr/lib64/ccache/bin:$PATH"
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#
unset ASFLAGS
unset LDFLAGS
unset CFLAGS
unset CXXFLAGS
unset FCFLAGS
unset FFLAGS
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
#
export CFLAGS="-fno-stack-protector -pthread -lpthread -static-libgcc -static-libstdc++ -O3 -fno-lto --param=lto-max-streaming-parallelism=16 -ffat-lto-objects -fomit-frame-pointer -fuse-ld=bfd -fuse-linker-plugin -march=native -mtune=native -Wall -Wl,-O2 -Wl,--build-id=sha1 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -malign-data=cacheline -Wl,-sort-common -fdevirtualize-at-ltrans -flifetime-dse=1 -Wl,--as-needed -fPIC -pipe -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -Wl,-z,max-page-size=0x1000 -feliminate-unused-debug-types -fno-semantic-interposition -m32 -mstackrealign"
export CXXFLAGS="-fno-stack-protector -pthread -lpthread -static-libgcc -static-libstdc++ -O3 -fno-lto --param=lto-max-streaming-parallelism=16 -ffat-lto-objects -fomit-frame-pointer -fuse-ld=bfd -fuse-linker-plugin -march=native -mtune=native -Wall -Wl,-O2 -Wl,--build-id=sha1 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -malign-data=cacheline -Wl,-sort-common -fdevirtualize-at-ltrans -flifetime-dse=1 -Wl,--as-needed -fPIC -pipe -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -Wl,-z,max-page-size=0x1000 -feliminate-unused-debug-types -fno-semantic-interposition -m32 -mstackrealign"
export LDFLAGS="-fno-stack-protector -pthread -lpthread -static-libgcc -static-libstdc++ -O3 -fno-lto --param=lto-max-streaming-parallelism=16 -ffat-lto-objects -fomit-frame-pointer -fuse-ld=bfd -fuse-linker-plugin -march=native -mtune=native -Wall -Wl,-O2 -Wl,--build-id=sha1 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -malign-data=cacheline -Wl,-sort-common -fdevirtualize-at-ltrans -flifetime-dse=1 -Wl,--as-needed -fPIC -pipe -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -Wl,-z,max-page-size=0x1000 -feliminate-unused-debug-types -fno-semantic-interposition -m32 -mstackrealign"
export ASFLAGS="--32"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
## altflags1_32 end
# pushd ..
# sd "flto=full" "flto=16" -r "*.cmake"
# popd
cmake -G Ninja ../llvm \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DLIB_INSTALL_DIR=%{_libdir} \
    -DLIB_SUFFIX=32 \
    -DLLVM_LIBDIR_SUFFIX=32 \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_C_COMPILER=gcc \
    -DCMAKE_CXX_COMPILER=g++ \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_SBINDIR=%{_sbindir} \
    -DLLVM_PARALLEL_COMPILE_JOBS:STRING=16 \
    -DLLVM_PARALLEL_LINK_JOBS:STRING=16 \
    -DCMAKE_AR=/usr/bin/gcc-ar \
    -DCMAKE_NM=/usr/bin/gcc-nm \
    -DCMAKE_RANLIB=/usr/bin/gcc-ranlib \
    -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
    -DENABLE_LINKER_BUILD_ID:BOOL=ON \
    -DCLANG_BUILD_TOOLS:BOOL=OFF \
    -DCLANG_DEFAULT_LINKER=lld \
    -DLLVM_ENABLE_LIBCXX:BOOL=OFF \
    -DLLVM_STATIC_LINK_CXX_STDLIB:BOOL=ON \
    -DCLANG_DEFAULT_CXX_STDLIB:STRING=libstdc++ \
    -DCLANG_ENABLE_STATIC_ANALYZER:BOOL=ON \
    -DCLANG_INCLUDE_TESTS:BOOL=OFF \
    -DCLANG_LINK_CLANG_DYLIB:BOOL=OFF \
    -DLLVM_LINK_LLVM_DYLIB:BOOL=OFF \
    -DLLVM_BUILD_LLVM_DYLIB:BOOL=ON \
    -DLIBCLANG_BUILD_STATIC:BOOL=ON \
    -DCOMPILER_RT_BUILD_SANITIZERS:BOOL=OFF \
    -DCOMPILER_RT_BUILD_XRAY:BOOL=OFF \
    -DLLVM_BINUTILS_INCDIR=/usr/include \
    -DLLVM_BUILD_EXAMPLES:BOOL=OFF \
    -DLLVM_BUILD_RUNTIME:BOOL=ON \
    -DLLVM_BUILD_TOOLS:BOOL=OFF \
    -DLLVM_BUILD_UTILS:BOOL=OFF \
    -DLLVM_TOOL_CLANG_BUILD:BOOL=OFF \
    -DLLVM_TOOL_LLD_BUILD:BOOL=OFF \
    -DLLVM_ENABLE_ASSERTIONS:BOOL=OFF \
    -DLLVM_ENABLE_BINDINGS:BOOL=OFF \
    -DLLVM_ENABLE_DOXYGEN:BOOL=OFF \
    -DLLVM_ENABLE_EH:BOOL=ON \
    -DLLVM_ENABLE_LIBXML2:BOOL=ON \
    -DLLVM_ENABLE_RTTI:BOOL=ON \
    -DLLVM_REQUIRES_RTTI:BOOL=ON \
    -DLLVM_ENABLE_THREADS:BOOL=ON \
    -DLLVM_ENABLE_Z3_SOLVER:BOOL=ON \
    -DLLVM_ENABLE_LIBEDIT:BOOL=OFF \
    -DLLVM_ENABLE_TERMINFO:BOOL=OFF \
    -DLLVM_ENABLE_ZLIB:BOOL=ON \
    -DLLVM_ENABLE_FFI:BOOL=ON \
    -DFFI_INCLUDE_DIR=`pkg-config --variable=includedir libffi` \
    -DCLANG_ENABLE_ARCMT:BOOL=OFF \
    -DLLVM_INCLUDE_TESTS:BOOL=OFF \
    -DLLVM_INCLUDE_TOOLS:BOOL=OFF \
    -DLLVM_INSTALL_UTILS:BOOL=OFF \
    -DCMAKE_DISABLE_FIND_PACKAGE_CUDA:BOOL=ON \
    -DLLVM_OPTIMIZED_TABLEGEN:BOOL=ON \
    -DLLVM_ENABLE_PIC=ON \
    -DLLVM_TARGETS_TO_BUILD="X86" \
    -DLLVM_TOOL_CLANG_TOOLS_EXTRA_BUILD:BOOL=OFF \
    -DLLVM_TOOL_COMPILER_RT_BUILD:BOOL=OFF \
    -DLLVM_USE_LINKER:STRING=bfd \
    -DLLVM_HOST_TRIPLE="x86_64-generic-linux" \
    -DPYTHON_EXECUTABLE:FILEPATH=/usr/bin/python3 \
    -DLLVM_ENABLE_PLUGINS:BOOL=ON \
    -DLLVM_EXPORT_SYMBOLS_FOR_PLUGINS:BOOL=ON \
    -DLLVM_ENABLE_PROJECTS="llvm;clang;clang-tools-extra;lld;parallel-libs;polly" \
    -DCMAKE_C_FLAGS="-fno-stack-protector -pthread -lpthread -static-libgcc -static-libstdc++ -O3 -fno-lto --param=lto-max-streaming-parallelism=16 -ffat-lto-objects -fomit-frame-pointer -fuse-ld=bfd -fuse-linker-plugin -march=native -mtune=native -Wall -Wl,-O2 -Wl,--build-id=sha1 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -malign-data=cacheline -Wl,-sort-common -fdevirtualize-at-ltrans -flifetime-dse=1 -Wl,--as-needed -fPIC -pipe -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -Wl,-z,max-page-size=0x1000 -feliminate-unused-debug-types -fno-semantic-interposition -m32 -mstackrealign" \
    -DCMAKE_CXX_FLAGS="-fno-stack-protector -pthread -lpthread -static-libgcc -static-libstdc++ -O3 -fno-lto --param=lto-max-streaming-parallelism=16 -ffat-lto-objects -fomit-frame-pointer -fuse-ld=bfd -fuse-linker-plugin -march=native -mtune=native -Wall -Wl,-O2 -Wl,--build-id=sha1 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -malign-data=cacheline -Wl,-sort-common -fdevirtualize-at-ltrans -flifetime-dse=1 -Wl,--as-needed -fPIC -pipe -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -Wl,-z,max-page-size=0x1000 -feliminate-unused-debug-types -fno-semantic-interposition -m32 -mstackrealign" \
    -DCMAKE_EXE_LINKER_FLAGS="-fno-stack-protector -pthread -lpthread -static-libgcc -static-libstdc++ -O3 -fno-lto --param=lto-max-streaming-parallelism=16 -ffat-lto-objects -fomit-frame-pointer -fuse-ld=bfd -fuse-linker-plugin -march=native -mtune=native -Wall -Wl,-O2 -Wl,--build-id=sha1 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -malign-data=cacheline -Wl,-sort-common -fdevirtualize-at-ltrans -flifetime-dse=1 -Wl,--as-needed -fPIC -pipe -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -Wl,-z,max-page-size=0x1000 -feliminate-unused-debug-types -fno-semantic-interposition -m32 -mstackrealign" \
    -DCMAKE_MODULE_LINKER_FLAGS="-fno-stack-protector -pthread -lpthread -static-libgcc -static-libstdc++ -O3 -fno-lto --param=lto-max-streaming-parallelism=16 -ffat-lto-objects -fomit-frame-pointer -fuse-ld=bfd -fuse-linker-plugin -march=native -mtune=native -Wall -Wl,-O2 -Wl,--build-id=sha1 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -malign-data=cacheline -Wl,-sort-common -fdevirtualize-at-ltrans -flifetime-dse=1 -Wl,--as-needed -fPIC -pipe -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -Wl,-z,max-page-size=0x1000 -feliminate-unused-debug-types -fno-semantic-interposition -m32 -mstackrealign" \
    -DCMAKE_SHARED_LINKER_FLAGS="-fno-stack-protector -pthread -lpthread -static-libgcc -static-libstdc++ -O3 -fno-lto --param=lto-max-streaming-parallelism=16 -ffat-lto-objects -fomit-frame-pointer -fuse-ld=bfd -fuse-linker-plugin -march=native -mtune=native -Wall -Wl,-O2 -Wl,--build-id=sha1 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -malign-data=cacheline -Wl,-sort-common -fdevirtualize-at-ltrans -flifetime-dse=1 -Wl,--as-needed -fPIC -pipe -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -Wl,-z,max-page-size=0x1000 -feliminate-unused-debug-types -fno-semantic-interposition -m32 -mstackrealign" \
    -DGCC_INSTALL_PREFIX="/usr" \
    -DLLVM_BUILD_32_BITS:BOOL=ON \
    -Wno-dev
ninja --verbose  %{?_smp_mflags}
## ccache stats
ccache -s
## ccache stats
unset PKG_CONFIG_PATH
popd

%install
export SOURCE_DATE_EPOCH=1621164519
rm -rf %{buildroot}
pushd clr-build32
%ninja_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
    pushd %{buildroot}/usr/lib32/pkgconfig
    for i in *.pc ; do ln -s $i 32$i ; done
    popd
fi
popd

%files
%defattr(-,root,root,-)
