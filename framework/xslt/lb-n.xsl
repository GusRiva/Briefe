<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:tei="http://www.tei-c.org/ns/1.0"
    exclude-result-prefixes="xs tei"
    version="2.0">
    
    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="tei:lb">
        <!--<xsl:text>&#x000A;</xsl:text>-->
        <lb xmlns="http://www.tei-c.org/ns/1.0" ><xsl:attribute name="n"><xsl:number count="tei:lb" level="any"></xsl:number></xsl:attribute></lb>
    </xsl:template>
    
    <xsl:template match="tei:pb">
        <xsl:variable name="simple_count">
            <xsl:number count="tei:pb" level="any"/>
        </xsl:variable>
        <pb xmlns="http://www.tei-c.org/ns/1.0" >
            <xsl:attribute name="n">
                <xsl:choose>
                    <xsl:when test="$simple_count mod 2 = 1">
                        <xsl:value-of select=" format-number( ( $simple_count + 0.9 ) div 2 , '##')"/>
                        <xsl:text>r</xsl:text>
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:value-of select=" format-number( ( $simple_count + 0.9 ) div 2 , '##')"/>
                        <xsl:text>v</xsl:text>
                    </xsl:otherwise>
                </xsl:choose>
                
                
            </xsl:attribute>
        </pb>
    </xsl:template>
    
    
</xsl:stylesheet>