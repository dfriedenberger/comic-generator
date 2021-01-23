import boto3
import argparse


def parse_args():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Script for creating mp3 from text via aws.')
    parser.add_argument("--voice", required=True,
                        metavar="VOICE",
                        help="Voice Id")
    parser.add_argument("--input", required=True,
                        metavar="INPUT",
                        help="ML input file")
    parser.add_argument("--output", required=True,
                        metavar="OUTPUT",
                        help="MP3 output file")
    args = parser.parse_args()

    return args.voice , args.input , args.output

voiceId , inputFile , outputFile = parse_args()

client = boto3.client('polly')


for lang in ['de-DE','es-ES']: #'en-GB','en-US'
    result = client.describe_voices(
        LanguageCode= lang, 
    )
    for voice in result['Voices']:
        print(voice['Id'],voice['LanguageCode'],voice['Gender'])

input = open(inputFile, "r")
text = input.read()

response = client.synthesize_speech(VoiceId=voiceId,
                OutputFormat='mp3', 
                Text = text)

file = open(outputFile, 'wb')
file.write(response['AudioStream'].read())
file.close()

