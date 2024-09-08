from seqbio.calculation.SeqCal  import *
from seqbio.pattern.SeqPattern  import *
from seqbio.seqMan.dnaconvert  import *

def test_main():
    seq = 'ATGGGccGTAGAATTCTTGCaaGCCCGT'
    seq = seq.upper()
    print("Transcription: ", dna2rna(seq))
    print("Transcription-revcomp: ", dna2rna(reverseComplementSeq(seq)))
    print("Translation: ", dna2protein(seq))
    print("Translation-revcomp: ", dna2protein(reverseComplementSeq(seq)))
    print("GC Content:", gcContent(seq))
    print("Count Bases: ", countBasesDict(seq))
    print("Count Bases-revcomp: ", countBasesDict(reverseComplementSeq(seq)))
    print("Search EcoRI: ", enzTargetsScan(seq, 'EcoRI'))
    print("Search EcoRI-revcomp: ", enzTargetsScan(reverseComplementSeq(seq), 'EcoRI'))

def argparserLocal():
    from argparse import ArgumentParser
    '''Argument parser for the commands'''
    parser = ArgumentParser(prog='myseq', description='Work with sequence')

    subparsers = parser.add_subparsers(
        title='commands', description='Please choose command below:',
        dest='command'
    )
    subparsers.required = True

    #SeqCal
    cgc_command = subparsers.add_parser('gcContent', help='Calculate GC content')
    cgc_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    
    count_command = subparsers.add_parser('countBases', help='Count number of each base')
    count_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    count_command.add_argument("-r", "--revcomp", action='store_true',
                            help="Convet DNA to reverse-complementary")

    #dnaconvert
    transcription_command = subparsers.add_parser('transcription', help='Convert DNA->RNA')
    transcription_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    transcription_command.add_argument("-r", "--revcomp", action='store_true',
                            help="Convet DNA to reverse-complementary")
    
    translation_command = subparsers.add_parser('translation', help='Convert DNA->Protein')
    translation_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    translation_command.add_argument("-r", "--revcomp", action='store_true',
                                help="Convet DNA to reverse-complementary")

    #SeqPattern
    enzTargetsScan_command = subparsers.add_parser('enzTargetsScan', help='Find restriction enzyme')
    enzTargetsScan_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    enzTargetsScan_command.add_argument("-e", "--enz", type=str, default=None,
                             help="Enzyme name")
    enzTargetsScan_command.add_argument("-r", "--revcomp", action='store_true',
                                help="Convet DNA to reverse-complementary")


    # parser.print_help()
    return parser

def main():
    parser = argparserLocal()
    args = parser.parse_args()

    if args.seq == None:
        print("------\nError: You do not provide -s or --seq\n------\n")
    else:
        seq = args.seq.upper()
    # Input
    # seq = 'ATGGGccGTAGAATTCTTGCaaGCCCGT'

    if args.command == 'gcContent':
        if args.seq == None:
            exit(parser.parse_args(['gcContent','-h']))
        print("Input",args.seq,"\nGC content =", gcContent(seq) )

    elif args.command == 'countBases':
        if args.seq == None:
            exit(parser.parse_args(['countBases','-h']))
        if args.revcomp == False:
            print("Input",args.seq,"\ncountBases =", countBasesDict(seq) )
        else :
            print("Input",args.seq,"\ncountBases =", countBasesDict(reverseComplementSeq(seq)) )

    elif args.command == 'transcription':
        if args.seq == None:
            exit(parser.parse_args(['transcription','-h']))
        if args.revcomp == False:
            print("Input",args.seq,"\nTranscription =", dna2rna(seq) )
        else :
            print("Input",args.seq,"\nTranscription =", dna2rna(reverseComplementSeq(seq)))

    elif args.command == 'translation':
        if args.seq == None:
            exit(parser.parse_args(['translation','-h']))
        if args.revcomp == False:
            print("Input",args.seq,"\nTranslation =", dna2protein(seq) )
        else :
            print("Input",args.seq,"\nTranslation =", dna2protein(reverseComplementSeq(seq)))

    elif args.command == 'enzTargetsScan':
        if args.seq == None or args.enz == None:
            exit(parser.parse_args(['enzTargetsScan','-h']))
        else:
            enz = args.enz
        if args.revcomp == False:
            # print("Input",args.seq,"\n",args.enz,"sites =", enzTargetsScan(seq, enz) )
            print(f"Input {args.seq}\n{args.enz} sites = {enzTargetsScan(seq, enz)}")
        else :
            # print("Input",args.seq,"\n",args.enz,"sites =", enzTargetsScan(reverseComplementSeq(seq), enz) )
            print(f"Input {args.seq}\n{args.enz} sites = {enzTargetsScan(reverseComplementSeq(seq), enz)}")      

# Input
if __name__ == '__main__':
    main()
    # test_main()