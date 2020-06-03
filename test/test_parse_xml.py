from collections import OrderedDict
from pprint import pprint

from src import parse


def test__parse__simple():
    _input = """
<aaa>
    <bbb>ccc</bbb>
</aaa>
"""

    expected = [
        {
            "attributes": {},
            "parent_path": "/",
            "path": "/aaa/",
            "tag": "aaa",
            "value": "",
        },
        {
            "attributes": {},
            "parent_path": "/aaa/",
            "path": "/aaa/bbb/",
            "tag": "bbb",
            "value": "ccc",
        },
    ]

    actual = parse.xml(_input)
    assert actual == expected


def test__parse__dict_list_simple():
    _input = """
<aaa>
    <bbb>ccc</bbb>
    <something>
        <ddd1>eee1</ddd1>
        <ddd2>eee2</ddd2>
    </something>
    <fff>ggg</fff>
</aaa>
"""

    expected = [
        {
            "attributes": {},
            "parent_path": "/",
            "path": "/aaa/",
            "tag": "aaa",
            "value": "",
        },
        {
            "attributes": {},
            "parent_path": "/aaa/",
            "path": "/aaa/bbb/",
            "tag": "bbb",
            "value": "ccc",
        },
        {
            "attributes": {},
            "parent_path": "/aaa/",
            "path": "/aaa/something/",
            "tag": "something",
            "value": "",
        },
        {
            "attributes": {},
            "parent_path": "/aaa/something/",
            "path": "/aaa/something/ddd1/",
            "tag": "ddd1",
            "value": "eee1",
        },
        {
            "attributes": {},
            "parent_path": "/aaa/something/",
            "path": "/aaa/something/ddd2/",
            "tag": "ddd2",
            "value": "eee2",
        },
        {
            "attributes": {},
            "parent_path": "/aaa/",
            "path": "/aaa/fff/",
            "tag": "fff",
            "value": "ggg",
        },
    ]

    actual = parse.xml(_input)
    assert actual == expected


def test__parse__multiple_siblings_simple():
    _input = """
<Vehicles>
    <Vehicle>
        <Type>Red Scooter</Type>
    </Vehicle>
    <Vehicle>
        <Type>Red Scooter</Type>
    </Vehicle>
</Vehicles>"""

    expected = [
        {
            "attributes": {},
            "parent_path": "/",
            "path": "/Vehicles/",
            "tag": "Vehicles",
            "value": "",
        },
        {
            "attributes": {},
            "parent_path": "/Vehicles/",
            "path": "/Vehicles/Vehicle/0/",
            "tag": "Vehicle",
            "value": "",
        },
        {
            "attributes": {},
            "parent_path": "/Vehicles/Vehicle/0/",
            "path": "/Vehicles/Vehicle/0/Type/",
            "tag": "Type",
            "value": "Red Scooter",
        },
        {
            "attributes": {},
            "parent_path": "/Vehicles/",
            "path": "/Vehicles/Vehicle/1/",
            "tag": "Vehicle",
            "value": "",
        },
        {
            "attributes": {},
            "parent_path": "/Vehicles/Vehicle/1/",
            "path": "/Vehicles/Vehicle/1/Type/",
            "tag": "Type",
            "value": "Red Scooter",
        },
    ]

    actual = parse.xml(_input)
    assert actual == expected


def test__parse__multiple_siblings():
    _input = """
<Policy>
    <FirstName>Jane</FirstName>
    <LastName>Smith</LastName>
    <Vehicles id="4">
        <Vehicle>
            <Type>Red Scooter</Type>
            <Premium>3000</Premium>
        </Vehicle>
        <Vehicle>
            <Type>Red Scooter</Type>
            <Premium>3000</Premium>
        </Vehicle>
    </Vehicles>
</Policy>
    """

    expected = [
        {
            "parent_path": "/",
            "path": "/Policy/",
            "tag": "Policy",
            "attributes": {},
            "value": "",
        },
        {
            "parent_path": "/Policy/",
            "path": "/Policy/FirstName/",
            "tag": "FirstName",
            "attributes": {},
            "value": "Jane",
        },
        {
            "parent_path": "/Policy/",
            "path": "/Policy/LastName/",
            "tag": "LastName",
            "attributes": {},
            "value": "Smith",
        },
        {
            "parent_path": "/Policy/",
            "path": "/Policy/Vehicles/",
            "tag": "Vehicles",
            "attributes": {"id": "4"},
            "value": "",
        },
        {
            "parent_path": "/Policy/Vehicles/",
            "path": "/Policy/Vehicles/Vehicle/0/",
            "tag": "Vehicle",
            "attributes": {},
            "value": "",
        },
        {
            "parent_path": "/Policy/Vehicles/Vehicle/0/",
            "path": "/Policy/Vehicles/Vehicle/0/Type/",
            "tag": "Type",
            "attributes": {},
            "value": "Red Scooter",
        },
        {
            "parent_path": "/Policy/Vehicles/Vehicle/0/",
            "path": "/Policy/Vehicles/Vehicle/0/Premium/",
            "tag": "Premium",
            "attributes": {},
            "value": "3000",
        },
        {
            "parent_path": "/Policy/Vehicles/",
            "path": "/Policy/Vehicles/Vehicle/1/",
            "tag": "Vehicle",
            "attributes": {},
            "value": "",
        },
        {
            "parent_path": "/Policy/Vehicles/Vehicle/1/",
            "path": "/Policy/Vehicles/Vehicle/1/Type/",
            "tag": "Type",
            "attributes": {},
            "value": "Red Scooter",
        },
        {
            "parent_path": "/Policy/Vehicles/Vehicle/1/",
            "path": "/Policy/Vehicles/Vehicle/1/Premium/",
            "tag": "Premium",
            "attributes": {},
            "value": "3000",
        },
    ]

    actual = parse.xml(_input)
    assert actual == expected


def test__parse__mixed_list():
    _input = """
<Policy>
    <FirstName>Jane</FirstName>
    <LastName>Smith</LastName>
    <Vehicles id="4">
        <Vehicle>
            <Type>Red Scooter</Type>
            <Premium>3000</Premium>
        </Vehicle>
        <Vehicle>
            <Type>Red Scooter</Type>
            <Premium>3000</Premium>
        </Vehicle>
        <NotVehicle>
            <Type>Red Scooter</Type>
            <Premium>3000</Premium>
        </NotVehicle>
    </Vehicles>
</Policy>
    """

    expected = [
        {
            "parent_path": "/",
            "path": "/Policy/",
            "tag": "Policy",
            "attributes": {},
            "value": "",
        },
        {
            "parent_path": "/Policy/",
            "path": "/Policy/FirstName/",
            "tag": "FirstName",
            "attributes": {},
            "value": "Jane",
        },
        {
            "parent_path": "/Policy/",
            "path": "/Policy/LastName/",
            "tag": "LastName",
            "attributes": {},
            "value": "Smith",
        },
        {
            "parent_path": "/Policy/",
            "path": "/Policy/Vehicles/",
            "tag": "Vehicles",
            "attributes": {"id": "4"},
            "value": "",
        },
        {
            "parent_path": "/Policy/Vehicles/",
            "path": "/Policy/Vehicles/Vehicle/0/",
            "tag": "Vehicle",
            "attributes": {},
            "value": "",
        },
        {
            "parent_path": "/Policy/Vehicles/Vehicle/0/",
            "path": "/Policy/Vehicles/Vehicle/0/Type/",
            "tag": "Type",
            "attributes": {},
            "value": "Red Scooter",
        },
        {
            "parent_path": "/Policy/Vehicles/Vehicle/0/",
            "path": "/Policy/Vehicles/Vehicle/0/Premium/",
            "tag": "Premium",
            "attributes": {},
            "value": "3000",
        },
        {
            "parent_path": "/Policy/Vehicles/",
            "path": "/Policy/Vehicles/Vehicle/1/",
            "tag": "Vehicle",
            "attributes": {},
            "value": "",
        },
        {
            "parent_path": "/Policy/Vehicles/Vehicle/1/",
            "path": "/Policy/Vehicles/Vehicle/1/Type/",
            "tag": "Type",
            "attributes": {},
            "value": "Red Scooter",
        },
        {
            "parent_path": "/Policy/Vehicles/Vehicle/1/",
            "path": "/Policy/Vehicles/Vehicle/1/Premium/",
            "tag": "Premium",
            "attributes": {},
            "value": "3000",
        },
        {
            "parent_path": "/Policy/Vehicles/",
            "path": "/Policy/Vehicles/NotVehicle/",
            "tag": "NotVehicle",
            "attributes": {},
            "value": "",
        },
        {
            "parent_path": "/Policy/Vehicles/NotVehicle/",
            "path": "/Policy/Vehicles/NotVehicle/Type/",
            "tag": "Type",
            "attributes": {},
            "value": "Red Scooter",
        },
        {
            "parent_path": "/Policy/Vehicles/NotVehicle/",
            "path": "/Policy/Vehicles/NotVehicle/Premium/",
            "tag": "Premium",
            "attributes": {},
            "value": "3000",
        },
    ]

    actual = parse.xml(_input)
    assert actual == expected


def test__parse__no_siblings():
    _input = """
<Policy>
    <FirstName>Jane</FirstName>
    <LastName>Smith</LastName>
    <Vehicles id="4">
        <Vehicle>
            <Type>Red Scooter</Type>
            <Premium>3000</Premium>
        </Vehicle>
    </Vehicles>
</Policy>
    """

    expected = [
        {
            "parent_path": "/",
            "path": "/Policy/",
            "tag": "Policy",
            "attributes": {},
            "value": "",
        },
        {
            "parent_path": "/Policy/",
            "path": "/Policy/FirstName/",
            "tag": "FirstName",
            "attributes": {},
            "value": "Jane",
        },
        {
            "parent_path": "/Policy/",
            "path": "/Policy/LastName/",
            "tag": "LastName",
            "attributes": {},
            "value": "Smith",
        },
        {
            "parent_path": "/Policy/",
            "path": "/Policy/Vehicles/",
            "tag": "Vehicles",
            "attributes": {"id": "4"},
            "value": "",
        },
        {
            "parent_path": "/Policy/Vehicles/",
            "path": "/Policy/Vehicles/Vehicle/",
            "tag": "Vehicle",
            "attributes": {},
            "value": "",
        },
        {
            "parent_path": "/Policy/Vehicles/Vehicle/",
            "path": "/Policy/Vehicles/Vehicle/Type/",
            "tag": "Type",
            "attributes": {},
            "value": "Red Scooter",
        },
        {
            "parent_path": "/Policy/Vehicles/Vehicle/",
            "path": "/Policy/Vehicles/Vehicle/Premium/",
            "tag": "Premium",
            "attributes": {},
            "value": "3000",
        },
    ]

    actual = parse.xml(_input)
    assert actual == expected


def test__parse__many_attributes():
    _input = """
<Policy id1="1A" id2="1B">
    <FirstName id1="2A" id2="2B">Jane</FirstName>
    <LastName id1="3A" id2="3B">Smith</LastName>
    <Vehicles id1="4A" id2="4B">
        <Vehicle id1="5A" id2="5B">
            <Type id1="6A" id2="6B">Red Scooter</Type>
            <Premium id1="7A" id2="7B">3000</Premium>
        </Vehicle>
    </Vehicles>
</Policy>
    """

    expected = [
        {
            "parent_path": "/",
            "path": "/Policy/",
            "tag": "Policy",
            "attributes": {"id1": "1A", "id2": "1B"},
            "value": "",
        },
        {
            "parent_path": "/Policy/",
            "path": "/Policy/FirstName/",
            "tag": "FirstName",
            "attributes": {"id1": "2A", "id2": "2B"},
            "value": "Jane",
        },
        {
            "parent_path": "/Policy/",
            "path": "/Policy/LastName/",
            "tag": "LastName",
            "attributes": {"id1": "3A", "id2": "3B"},
            "value": "Smith",
        },
        {
            "parent_path": "/Policy/",
            "path": "/Policy/Vehicles/",
            "tag": "Vehicles",
            "attributes": {"id1": "4A", "id2": "4B"},
            "value": "",
        },
        {
            "parent_path": "/Policy/Vehicles/",
            "path": "/Policy/Vehicles/Vehicle/",
            "tag": "Vehicle",
            "attributes": {"id1": "5A", "id2": "5B"},
            "value": "",
        },
        {
            "parent_path": "/Policy/Vehicles/Vehicle/",
            "path": "/Policy/Vehicles/Vehicle/Type/",
            "tag": "Type",
            "attributes": {"id1": "6A", "id2": "6B"},
            "value": "Red Scooter",
        },
        {
            "parent_path": "/Policy/Vehicles/Vehicle/",
            "path": "/Policy/Vehicles/Vehicle/Premium/",
            "tag": "Premium",
            "attributes": {"id1": "7A", "id2": "7B"},
            "value": "3000",
        },
    ]

    actual = parse.xml(_input)
    assert actual == expected


def test__parse__strange_hybrid_tag():
    _input = """
<a>
    <b> Something something
        <b1>IMPORTANT TEXT</b1>
        <b2>YOU WILL DIE</b2>
    </b>
    <c>Blah blah</c>
</a>
"""

    expected = [
        {"parent_path": "/", "path": "/a/", "tag": "a", "attributes": {}, "value": ""},
        {
            "parent_path": "/a/",
            "path": "/a/b/",
            "tag": "b",
            "attributes": {},
            "value": "Something something",
        },
        {
            "parent_path": "/a/b/",
            "path": "/a/b/b1/",
            "tag": "b1",
            "attributes": {},
            "value": "IMPORTANT TEXT",
        },
        {
            "parent_path": "/a/b/",
            "path": "/a/b/b2/",
            "tag": "b2",
            "attributes": {},
            "value": "YOU WILL DIE",
        },
        {
            "parent_path": "/a/",
            "path": "/a/c/",
            "tag": "c",
            "attributes": {},
            "value": "Blah blah",
        },
    ]

    actual = parse.xml(_input)
    assert actual == expected


def test__parse__ugly_xml():
    _input = """
<GrossData>
  <Policy id='57' type='bundle'>
      <FirstName>Joe</FirstName>
      <FirstName>Boris</FirstName>
      <LastName>Rochette</LastName>
      <Vehicles id="4">
          <Vehicle>
              <Type>Red Scooter</Type>
              <Premium>3000</Premium>
          </Vehicle>
          <Vehicle>
              <Type>Red Scooter</Type>
              <Premium>3000</Premium>
          </Vehicle>
          <Vehicle id="Xzibit">
              <Type>Blue Scooter</Type>
              <Premium>2800</Premium>
                <AddlCharge>1300</AddlCharge>
          </Vehicle>
          <Vehicle>
            <Type>Huge Yacht</Type>
          </Vehicle>
      </Vehicles>
  </Policy>
  <Policy id="randompolicyid">
      <FirstName>Mary</FirstName>
      <LastName>McFakeName</LastName>
      <MiddleName>Marjorie</MiddleName>
      <Vehicles id="4">
          <Vehicle>
              <Type>Skateboard</Type>
              <Premium>2000</Premium>
                <AddlCharge>5</AddlCharge>
                <Wheels>
                  <RoundOnes>
                    <Premium>500</Premium>
                  </RoundOnes>
                </Wheels>
          </Vehicle>
          <Vehicle>
              <Type>Red Scooter</Type>
              <Premium>3000</Premium>
          </Vehicle>
          <Vehicle id="MyHoopty">
              <Type>Blue Scooter</Type>
              <Premium>2800</Premium>
                <AddlCharge>1300</AddlCharge>
          </Vehicle>
          <Vehicle>
            <Type>Huge Yacht</Type>
              <SubVehicle>
                <Type>Red Scooter</Type>
                <Premium>200</Premium>
              </SubVehicle>
          </Vehicle>
      </Vehicles>
  </Policy>
</GrossData>
    """

    expected = [
        {
            "parent_path": "/",
            "path": "/GrossData/",
            "tag": "GrossData",
            "attributes": {},
            "value": "",
        },
        {
            "parent_path": "/GrossData/",
            "path": "/GrossData/Policy/0/",
            "tag": "Policy",
            "attributes": {"id": "57", "type": "bundle"},
            "value": "",
        },
        {
            "parent_path": "/GrossData/Policy/0/",
            "path": "/GrossData/Policy/0/FirstName/0/",
            "tag": "FirstName",
            "attributes": {},
            "value": "Joe",
        },
        {
            "parent_path": "/GrossData/Policy/0/",
            "path": "/GrossData/Policy/0/FirstName/1/",
            "tag": "FirstName",
            "attributes": {},
            "value": "Boris",
        },
        {
            "parent_path": "/GrossData/Policy/0/",
            "path": "/GrossData/Policy/0/LastName/",
            "tag": "LastName",
            "attributes": {},
            "value": "Rochette",
        },
        {
            "parent_path": "/GrossData/Policy/0/",
            "path": "/GrossData/Policy/0/Vehicles/",
            "tag": "Vehicles",
            "attributes": {"id": "4"},
            "value": "",
        },
        {
            "parent_path": "/GrossData/Policy/0/Vehicles/",
            "path": "/GrossData/Policy/0/Vehicles/Vehicle/0/",
            "tag": "Vehicle",
            "attributes": {},
            "value": "",
        },
        {
            "parent_path": "/GrossData/Policy/0/Vehicles/Vehicle/0/",
            "path": "/GrossData/Policy/0/Vehicles/Vehicle/0/Type/",
            "tag": "Type",
            "attributes": {},
            "value": "Red Scooter",
        },
        {
            "parent_path": "/GrossData/Policy/0/Vehicles/Vehicle/0/",
            "path": "/GrossData/Policy/0/Vehicles/Vehicle/0/Premium/",
            "tag": "Premium",
            "attributes": {},
            "value": "3000",
        },
        {
            "parent_path": "/GrossData/Policy/0/Vehicles/",
            "path": "/GrossData/Policy/0/Vehicles/Vehicle/1/",
            "tag": "Vehicle",
            "attributes": {},
            "value": "",
        },
        {
            "parent_path": "/GrossData/Policy/0/Vehicles/Vehicle/1/",
            "path": "/GrossData/Policy/0/Vehicles/Vehicle/1/Type/",
            "tag": "Type",
            "attributes": {},
            "value": "Red Scooter",
        },
        {
            "parent_path": "/GrossData/Policy/0/Vehicles/Vehicle/1/",
            "path": "/GrossData/Policy/0/Vehicles/Vehicle/1/Premium/",
            "tag": "Premium",
            "attributes": {},
            "value": "3000",
        },
        {
            "parent_path": "/GrossData/Policy/0/Vehicles/",
            "path": "/GrossData/Policy/0/Vehicles/Vehicle/2/",
            "tag": "Vehicle",
            "attributes": {"id": "Xzibit"},
            "value": "",
        },
        {
            "parent_path": "/GrossData/Policy/0/Vehicles/Vehicle/2/",
            "path": "/GrossData/Policy/0/Vehicles/Vehicle/2/Type/",
            "tag": "Type",
            "attributes": {},
            "value": "Blue Scooter",
        },
        {
            "parent_path": "/GrossData/Policy/0/Vehicles/Vehicle/2/",
            "path": "/GrossData/Policy/0/Vehicles/Vehicle/2/Premium/",
            "tag": "Premium",
            "attributes": {},
            "value": "2800",
        },
        {
            "parent_path": "/GrossData/Policy/0/Vehicles/Vehicle/2/",
            "path": "/GrossData/Policy/0/Vehicles/Vehicle/2/AddlCharge/",
            "tag": "AddlCharge",
            "attributes": {},
            "value": "1300",
        },
        {
            "parent_path": "/GrossData/Policy/0/Vehicles/",
            "path": "/GrossData/Policy/0/Vehicles/Vehicle/3/",
            "tag": "Vehicle",
            "attributes": {},
            "value": "",
        },
        {
            "parent_path": "/GrossData/Policy/0/Vehicles/Vehicle/3/",
            "path": "/GrossData/Policy/0/Vehicles/Vehicle/3/Type/",
            "tag": "Type",
            "attributes": {},
            "value": "Huge Yacht",
        },
        {
            "parent_path": "/GrossData/",
            "path": "/GrossData/Policy/1/",
            "tag": "Policy",
            "attributes": {"id": "randompolicyid"},
            "value": "",
        },
        {
            "parent_path": "/GrossData/Policy/1/",
            "path": "/GrossData/Policy/1/FirstName/",
            "tag": "FirstName",
            "attributes": {},
            "value": "Mary",
        },
        {
            "parent_path": "/GrossData/Policy/1/",
            "path": "/GrossData/Policy/1/LastName/",
            "tag": "LastName",
            "attributes": {},
            "value": "McFakeName",
        },
        {
            "parent_path": "/GrossData/Policy/1/",
            "path": "/GrossData/Policy/1/MiddleName/",
            "tag": "MiddleName",
            "attributes": {},
            "value": "Marjorie",
        },
        {
            "parent_path": "/GrossData/Policy/1/",
            "path": "/GrossData/Policy/1/Vehicles/",
            "tag": "Vehicles",
            "attributes": {"id": "4"},
            "value": "",
        },
        {
            "parent_path": "/GrossData/Policy/1/Vehicles/",
            "path": "/GrossData/Policy/1/Vehicles/Vehicle/0/",
            "tag": "Vehicle",
            "attributes": {},
            "value": "",
        },
        {
            "parent_path": "/GrossData/Policy/1/Vehicles/Vehicle/0/",
            "path": "/GrossData/Policy/1/Vehicles/Vehicle/0/Type/",
            "tag": "Type",
            "attributes": {},
            "value": "Skateboard",
        },
        {
            "parent_path": "/GrossData/Policy/1/Vehicles/Vehicle/0/",
            "path": "/GrossData/Policy/1/Vehicles/Vehicle/0/Premium/",
            "tag": "Premium",
            "attributes": {},
            "value": "2000",
        },
        {
            "parent_path": "/GrossData/Policy/1/Vehicles/Vehicle/0/",
            "path": "/GrossData/Policy/1/Vehicles/Vehicle/0/AddlCharge/",
            "tag": "AddlCharge",
            "attributes": {},
            "value": "5",
        },
        {
            "parent_path": "/GrossData/Policy/1/Vehicles/Vehicle/0/",
            "path": "/GrossData/Policy/1/Vehicles/Vehicle/0/Wheels/",
            "tag": "Wheels",
            "attributes": {},
            "value": "",
        },
        {
            "parent_path": "/GrossData/Policy/1/Vehicles/Vehicle/0/Wheels/",
            "path": "/GrossData/Policy/1/Vehicles/Vehicle/0/Wheels/RoundOnes/",
            "tag": "RoundOnes",
            "attributes": {},
            "value": "",
        },
        {
            "parent_path": "/GrossData/Policy/1/Vehicles/Vehicle/0/Wheels/RoundOnes/",
            "path": "/GrossData/Policy/1/Vehicles/Vehicle/0/Wheels/RoundOnes/Premium/",
            "tag": "Premium",
            "attributes": {},
            "value": "500",
        },
        {
            "parent_path": "/GrossData/Policy/1/Vehicles/",
            "path": "/GrossData/Policy/1/Vehicles/Vehicle/1/",
            "tag": "Vehicle",
            "attributes": {},
            "value": "",
        },
        {
            "parent_path": "/GrossData/Policy/1/Vehicles/Vehicle/1/",
            "path": "/GrossData/Policy/1/Vehicles/Vehicle/1/Type/",
            "tag": "Type",
            "attributes": {},
            "value": "Red Scooter",
        },
        {
            "parent_path": "/GrossData/Policy/1/Vehicles/Vehicle/1/",
            "path": "/GrossData/Policy/1/Vehicles/Vehicle/1/Premium/",
            "tag": "Premium",
            "attributes": {},
            "value": "3000",
        },
        {
            "parent_path": "/GrossData/Policy/1/Vehicles/",
            "path": "/GrossData/Policy/1/Vehicles/Vehicle/2/",
            "tag": "Vehicle",
            "attributes": {"id": "MyHoopty"},
            "value": "",
        },
        {
            "parent_path": "/GrossData/Policy/1/Vehicles/Vehicle/2/",
            "path": "/GrossData/Policy/1/Vehicles/Vehicle/2/Type/",
            "tag": "Type",
            "attributes": {},
            "value": "Blue Scooter",
        },
        {
            "parent_path": "/GrossData/Policy/1/Vehicles/Vehicle/2/",
            "path": "/GrossData/Policy/1/Vehicles/Vehicle/2/Premium/",
            "tag": "Premium",
            "attributes": {},
            "value": "2800",
        },
        {
            "parent_path": "/GrossData/Policy/1/Vehicles/Vehicle/2/",
            "path": "/GrossData/Policy/1/Vehicles/Vehicle/2/AddlCharge/",
            "tag": "AddlCharge",
            "attributes": {},
            "value": "1300",
        },
        {
            "parent_path": "/GrossData/Policy/1/Vehicles/",
            "path": "/GrossData/Policy/1/Vehicles/Vehicle/3/",
            "tag": "Vehicle",
            "attributes": {},
            "value": "",
        },
        {
            "parent_path": "/GrossData/Policy/1/Vehicles/Vehicle/3/",
            "path": "/GrossData/Policy/1/Vehicles/Vehicle/3/Type/",
            "tag": "Type",
            "attributes": {},
            "value": "Huge Yacht",
        },
        {
            "parent_path": "/GrossData/Policy/1/Vehicles/Vehicle/3/",
            "path": "/GrossData/Policy/1/Vehicles/Vehicle/3/SubVehicle/",
            "tag": "SubVehicle",
            "attributes": {},
            "value": "",
        },
        {
            "parent_path": "/GrossData/Policy/1/Vehicles/Vehicle/3/SubVehicle/",
            "path": "/GrossData/Policy/1/Vehicles/Vehicle/3/SubVehicle/Type/",
            "tag": "Type",
            "attributes": {},
            "value": "Red Scooter",
        },
        {
            "parent_path": "/GrossData/Policy/1/Vehicles/Vehicle/3/SubVehicle/",
            "path": "/GrossData/Policy/1/Vehicles/Vehicle/3/SubVehicle/Premium/",
            "tag": "Premium",
            "attributes": {},
            "value": "200",
        },
    ]

    actual = parse.xml(_input)
    assert actual == expected


def test__parse__leaf_attributes():
    data = """<Type id="456">Red Scooter</Type>"""

    expected = [
        {
            "parent_path": "/",
            "path": "/Type/",
            "tag": "Type",
            "attributes": {"id": "456"},
            "value": "Red Scooter",
        }
    ]

    actual = parse.xml(data)
    assert actual == expected


def test__parse__leaf_attributes():
    data = """
<session id="lBdJGEbcO" > Some_text
    <subone> BLAH
        <subtwo policy="Car" > Some_subtwo_text
            <wn id="ygGTPGI" > 1 OF 3 IMPORTANT TEXTS</wn>
            <wn>2 OF 3 IMPORTANT TEXTS</wn>
            <b> 3 OF 3 IMPORTANT TEXTS</b>
        </subtwo>
    </subone>
</session>
    """

    expected = [
        {
            "parent_path": "/",
            "path": "/session/",
            "tag": "session",
            "attributes": {"id": "lBdJGEbcO"},
            "value": "Some_text",
        },
        {
            "parent_path": "/session/",
            "path": "/session/subone/",
            "tag": "subone",
            "attributes": {},
            "value": "BLAH",
        },
        {
            "parent_path": "/session/subone/",
            "path": "/session/subone/subtwo/",
            "tag": "subtwo",
            "attributes": {"policy": "Car"},
            "value": "Some_subtwo_text",
        },
        {
            "parent_path": "/session/subone/subtwo/",
            "path": "/session/subone/subtwo/wn/0/",
            "tag": "wn",
            "attributes": {"id": "ygGTPGI"},
            "value": "1 OF 3 IMPORTANT TEXTS",
        },
        {
            "parent_path": "/session/subone/subtwo/",
            "path": "/session/subone/subtwo/wn/1/",
            "tag": "wn",
            "attributes": {},
            "value": "2 OF 3 IMPORTANT TEXTS",
        },
        {
            "parent_path": "/session/subone/subtwo/",
            "path": "/session/subone/subtwo/b/",
            "tag": "b",
            "attributes": {},
            "value": "3 OF 3 IMPORTANT TEXTS",
        },
    ]

    actual = parse.xml(data)
    assert actual == expected


def _test__parse__multiple_strings():
    data = """
<a>
    string 1
    <b></b>
    string 2
    <c></c>
    string 3
</a>
    """

    expected = [
        {
            "attributes": {},
            "parent_path": "/",
            "path": "/a/",
            "tag": "a",
            "value": "string 1\n    \n    string 2\n    \n    string 3",
        },
        {
            "attributes": {},
            "parent_path": "/a/",
            "path": "/a/b/",
            "tag": "b",
            "value": "",
        },
        {
            "attributes": {},
            "parent_path": "/a/",
            "path": "/a/c/",
            "tag": "c",
            "value": "",
        },
    ]

    actual = parse.xml(data)
    assert actual == expected
