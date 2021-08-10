import json
import genson
import sys


class JSONSchemaGenerator:
    '''
    JSONSchemaGenerator creates json schema file for the json file provided as parameter.
    '''

    def gen_schema(file_name):
        with open(file_name) as data_file:
            doc = json.loads(data_file.read())
        builder = genson.SchemaBuilder()
        builder.add_object(doc)
        return builder.to_schema()

    def GenerateSchema(file_path):
        '''
        GenerateSchema is a function which generates schema file for the json data file provided as parameter to this function.
        It also writes the schema file with at the same directory with the filename appended with _schema.
        For Eg:
        If filepath (parameter to this function) = ./ExampleFile.json
        Then it will save the schema file as ./ExampleFile_schema.json at the same directory as that of Data File.
        '''
        schema_file_path = file_path.replace('.json', '_Schema.json')
        with open(schema_file_path, 'w') as out_file:
            json_schema = JSONSchemaGenerator.gen_schema(file_path)
            json_schema.update({'additionalProperties': False})
            json.dump(json_schema, out_file, indent=4)
        print('Schema generated:',schema_file_path)


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        JSONSchemaGenerator.GenerateSchema(file_path)
    except IndexError as e:
        print('Json file path is mandatory to provide.')
