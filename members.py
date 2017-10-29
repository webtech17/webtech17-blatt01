# coding: utf-8
# Uni Osnabrück, Web-Technologien 2017/2018
# Übungsblatt 01, Aufgabe 1-3
#

# https://docs.python.org/3/library/json.html
import json


def read_json(fn):
    """Read a members-json file from the file identified by fn. Content is parsed but not validated."""
    pass
    try:
        with open(fn) as json_data:
            data = json.load(json_data)
            return data
    except ValueError as e: #error if the passed string isn't valid json.
        print("The given file isn't a JSON file")
        print(e)


def print_html(fn, name, members):
    """Print HTML table to file 'fn'. Uses 'name' for heading and walks through 'members' structure."""
    try:
        f = open(fn, "w")
        infos = members
        header = "<h1>%s</h1>" % name
        f.write(header)
        i = 0
        while i < infos.__len__():# this part will be executes as long as there is mmore members.
            table = ("""
            <table>      <!-- Markiert den Beginn einer Tabelle -->
            <tr>       <!-- table row = Markiert Beginn einer Zeile -->
            <td>     <!-- table data = Markiert den Beginn einer Tabellenzelle -->
            Der Vorname: 
            </td>    <!-- markiert das Ende der Zelle -->
            <td>
            %s
             </td>
            </tr>      <!-- markiert das Ende der ersten Zeile -->
            <tr>
            <td>Der Nachname: </td>
            <td> %s</td>
            </tr>
            <tr>
            <td>Github-Benutzername: </td>
            <td> %s</td>
            </tr>
            <tr> 
            <td>Stud.IP-Benutzername: </td>
            <td> %s</td>
             </tr>
            </table>
                """ %(infos[i].get('firstname'), infos[i].get('lastname'),
                    infos[i].get('githubname'), infos[i].get('studipname')))
            f.write(table)
            i += 1
        f.close()
    except FileNotFoundError as e: # error will be thrown in case the file was not found
        print("file not found")
        print(e)
    except PermissionError as e: # error will be thrwn in case the permission to change file's content was denied
        print("No permisson to change the file's content")
        print(e)


if __name__ == '__main__':  # Python jargon for main - only executed if script is used as top level script
    infile = "members.json"
    outfile = "members.html"
    data = read_json(infile)
    print_html(outfile, data["name"], data["members"])
    print("HTML table written to '{}'".format(outfile))
