import json
import xmltodict

print (json.dumps(xmltodict.parse("""
    <mydocument has="an attribute">
        <and>
            <many>elements</many>
            <many>more elements</many>
        </and>
        <plus a="complex">
            element as well
        </plus>
    </mydocument>
    """), indent=4))
{
    "mydocument": {
        "@has": "an attribute", 
        "and": {
            "many": [
                "elements", 
                "more elements"
            ]
        }, 
        "plus": {
            "@a": "complex", 
            "#text": "element as well"
        }
    }
}
