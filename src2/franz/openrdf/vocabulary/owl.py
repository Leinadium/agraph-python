#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable-msg=C0103

##***** BEGIN LICENSE BLOCK *****
##Version: MPL 1.1
##
##The contents of this file are subject to the Mozilla Public License Version
##1.1 (the "License"); you may not use this file except in compliance with
##the License. You may obtain a copy of the License at
##http:##www.mozilla.org/MPL/
##
##Software distributed under the License is distributed on an "AS IS" basis,
##WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
##for the specific language governing rights and limitations under the
##License.
##
##The Original Code is the AllegroGraph Java Client interface.
##
##The Original Code was written by Franz Inc.
##Copyright (C) 2006 Franz Inc.  All Rights Reserved.
##
##***** END LICENSE BLOCK *****

from __future__ import absolute_import

from ..model.value import URI 

NS = "http://www.w3.org/2002/07/owl#"

class OWL:
    """
    A 'static' class containing useful OWL URIs.
    """

    NAMESPACE = NS
    CLASS = URI(namespace=NS, localname="Class")
    INDIVIDUAL = URI(namespace=NS, localname="Individual")
    EQUIVALENTCLASS = URI(namespace=NS, localname="equivalentClass")
    EQUIVALENTPROPERTY = URI(namespace=NS, localname="equivalentProperty")
    SAMEAS = URI(namespace=NS, localname="sameAs")
    DIFFERENTFROM = URI(namespace=NS, localname="differentFrom")
    ALLDIFFERENT = URI(namespace=NS, localname="AllDifferent")
    DISTINCTMEMBERS = URI(namespace=NS, localname="distinctMembers")
    OBJECTPROPERTY = URI(namespace=NS, localname="ObjectProperty")
    DATATYPEPROPERTY = URI(namespace=NS, localname="DatatypeProperty")
    INVERSEOF = URI(namespace=NS, localname="inverseOf")
    TRANSITIVEPROPERTY = URI(namespace=NS, localname="TransitiveProperty")
    SYMMETRICPROPERTY = URI(namespace=NS, localname="SymmetricProperty")
    FUNCTIONALPROPERTY = URI(namespace=NS, localname="FunctionalProperty")
    INVERSEFUNCTIONALPROPERTY = URI(namespace=NS,
	localname="InverseFunctionalProperty")
    RESTRICTION = URI(namespace=NS, localname="Restriction")
    ONPROPERTY = URI(namespace=NS, localname="onProperty")
    ALLVALUESFROM = URI(namespace=NS, localname="allValuesFrom")
    SOMEVALUESFROM = URI(namespace=NS, localname="someValuesFrom")
    MINCARDINALITY = URI(namespace=NS, localname="minCardinality")
    MAXCARDINALITY = URI(namespace=NS, localname="maxCardinality")
    CARDINALITY = URI(namespace=NS, localname="cardinality")
    ONTOLOGY = URI(namespace=NS, localname="Ontology")
    IMPORTS = URI(namespace=NS, localname="imports")
    INTERSECTIONOF = URI(namespace=NS, localname="intersectionOf")
    VERSIONINFO = URI(namespace=NS, localname="versionInfo")
    PRIORVERSION = URI(namespace=NS, localname="priorVersion")
    BACKWARDCOMPATIBLEWITH = URI(namespace=NS,
	localname="backwardCompatibleWith")
    INCOMPATIBLEWITH = URI(namespace=NS, localname="incompatibleWith")
    DEPRECATEDCLASS = URI(namespace=NS, localname="DeprecatedClass")
    DEPRECATEDPROPERTY = URI(namespace=NS, localname="DeprecatedProperty")
    ANNOTATIONPROPERTY = URI(namespace=NS, localname="AnnotationProperty")
    ONTOLOGYPROPERTY = URI(namespace=NS, localname="OntologyProperty")
    ## OWL DL and OWL Full
    ONEOF = URI(namespace=NS, localname="oneOf")
    HASVALUE = URI(namespace=NS, localname="hasValue")
    DISJOINTWITH = URI(namespace=NS, localname="disjointWith")
    UNIONOF = URI(namespace=NS, localname="unionOf")
    COMPLEMENTOF = URI(namespace=NS, localname="complementOf")
        
    ## map of uri strings to URI objects:
    uristr2obj = {}

for name, uri in OWL.__dict__.iteritems():
    if name.upper() == name:
        OWL.uristr2obj[str(uri)] = uri

del OWL.uristr2obj[NS]
