<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" 
    exclude-result-prefixes="xs"
    version="2.0">
    
    
    <xsl:template match="listPlace">
        <listPlace>
            <xsl:for-each select="place">
            <xsl:sort select="placeName"/>
            <place>
                <placeName><xsl:value-of select="placeName"/></placeName>
                <idno><xsl:value-of select="idno"/></idno>                
            </place>
            </xsl:for-each>
        </listPlace>
    </xsl:template>
    
    
    
    
</xsl:stylesheet>