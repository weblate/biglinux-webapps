# Maintainer: Bruno Goncalves <bigbruno@gmail.com>

pkgname=biglinux-webapps
pkgver=3.0.5
pkgrel=2
arch=('any')
license=('GPL')
url="https://github.com/biglinux/biglinux-webapps"
pkgdesc="Installs and removes BigLinux WebApps"
depends=('bigbashview' 'python-bs4' 'python-requests')
source=("git+https://github.com/biglinux/biglinux-webapps.git")
md5sums=(SKIP)


package() {
    cp -r "${srcdir}/biglinux-webapps/biglinux-webapps/usr/" "${pkgdir}/"
    cp -r "${srcdir}/biglinux-webapps/biglinux-webapps/etc/" "${pkgdir}/"
}


