# New ports collection makefile for:	freq
# Date created:				..
# Whom:					Daniel Burdakov <kreved@kreved.org>
#
# ~~~
#

PORTNAME=	freqbot
PORTVERSION=	1.0.99.169
CATEGORIES=	net-im
MASTER_SITES=	http://kreved.org/files/
DISTNAME=	${PORTNAME}-${PORTVERSION}

MAINTAINER=	kreved@kreved.org
COMMENT=	A Jabber bot

LIB_DEPENDS=	
BUILD_DEPENDS=	${PYTHON_SITELIBDIR}/twisted/__init__.py:${PORTSDIR}/devel/py-twistedCore \
		${PYTHON_SITELIBDIR}/twisted/web/__init__.py:${PORTSDIR}/www/py-twistedWeb

RUN_DEPENDS=	${PYTHON_SITELIBDIR}/twisted/__init__.py:${PORTSDIR}/devel/py-twistedCore \
		${PYTHON_SITELIBDIR}/twisted/web/__init__.py:${PORTSDIR}/www/py-twistedWeb \
		${PYTHON_SITELIBDIR}/twisted/words/__init__.py:${PORTSDIR}/net-im/py-twistedWords

USE_BZIP2=	yes
USE_PYTHON=	yes
USE_GMAKE=	yes
LOCAL_PYTHON=	${PYTHON_CMD}
#USE_RC_SUBR=	freq

ALL_TARGET=	build

.include <bsd.port.pre.mk>
.include <bsd.port.post.mk>