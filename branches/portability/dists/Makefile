# New ports collection makefile for:	freqbot
# Date created:				29 April 2008
# Whom:					Daniel Burdakov <kreved@kreved.org>
#
# $FreeBSD$
#

PORTNAME=	freqbot
PORTVERSION=	0.0
CATEGORIES=	net-im
MASTER_SITES=	http://kreved.org/files/freqbot/tarballs/
DISTNAME=	${PORTNAME}-${PORTVERSION}

MAINTAINER=	kreved@kreved.org
COMMENT=	Python Jabber bot

LIB_DEPENDS=
RUN_DEPENDS=	${PYTHON_SITELIBDIR}/twisted/__init__.py:${PORTSDIR}/devel/py-twistedCore \
		${PYTHON_SITELIBDIR}/twisted/web/__init__.py:${PORTSDIR}/www/py-twistedWeb \
		${PYTHON_SITELIBDIR}/twisted/words/__init__.py:${PORTSDIR}/net-im/py-twistedWords
BUILD_DEPENDS=	${PYTHON_SITELIBDIR}/twisted/__init__.py:${PORTSDIR}/devel/py-twistedCore \
		${PYTHON_SITELIBDIR}/twisted/web/__init__.py:${PORTSDIR}/www/py-twistedWeb \
		${PYTHON_SITELIBDIR}/twisted/words/__init__.py:${PORTSDIR}/net-im/py-twistedWords

GNU_CONFIGURE=	yes
CONFIGURE_TARGET=--build=${MACHINE_ARCH}-portbld-freebsd${OSREL}
USE_BZIP2=	yes
USE_PYTHON=	yes
LOCAL_PYTHON=	${PYTHON_CMD}

ALL_TARGET=	build

.include <bsd.port.pre.mk>
.include <bsd.port.post.mk>
