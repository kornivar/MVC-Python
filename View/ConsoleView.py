from Controller.DNKController import DNKController
from Model.SequenceModel import SequenceModel


class ConsoleView:
    def __init__(self):
        self.__dnkController = DNKController()

    def print_menu(self):
        print("""=== DNA/RNA MVC Console ===
            1) Input or update sequence
            2) Validate sequence
            3) Transcribe DNA -> RNA
            4) Reverse transcribe RNA -> DNA
            5) Reverse complement
            6) Show GC% and length
            7) Mutate base
            0) Exit
            """)

    def prompt(self, msg):
        return input(msg)

    def show(self, msg):
        print(msg)

    def show_sequence(self):
        seq = self.__dnkController.get_sequence()
        print(f"Current sequence: {seq if seq else '(none)'}")

    def run(self):
        while True:
            self.print_menu()
            choice = self.prompt("Choose option: ").strip()
            if choice == "1":
                user_input = self.prompt("Enter a DNA/RNA sequence: ").strip()
                if user_input == "":
                    self.show("Empty sequence. Nothing changed.")
                else:
                    model = SequenceModel(user_input.upper())
                    self.__dnkController.add_seq(model)
                    self.show("Sequence updated.")
                    self.show_sequence()
            elif choice == "2":
                seq = self.__dnkController.get_sequence()
                if not seq:
                    self.show("No sequence. Use option 1 to add one.")
                else:
                    res = self.__dnkController.validate(seq)
                    if res == -1:
                        self.show("Incorrect sequence.")
                    elif res == 0:
                        self.show("Sequence type: DNA")
                    else:
                        self.show("Sequence type: RNA")
            elif choice == "3":
                seq = self.__dnkController.get_sequence()
                if not seq:
                    self.show("No sequence. Use option 1 to add one.")
                else:
                    new_seq = self.__dnkController.transcribe(seq)
                    if new_seq is None:
                        self.show("Transcription failed: sequence is not DNA.")
                    else:
                        self.__dnkController.add_seq(SequenceModel(new_seq))
                        self.show("Transcribed DNA -> RNA.")
                        self.show_sequence()
            elif choice == "4":
                seq = self.__dnkController.get_sequence()
                if not seq:
                    self.show("No sequence. Use option 1 to add one.")
                else:
                    new_seq = self.__dnkController.reverse_transcribe(seq)
                    if new_seq is None:
                        self.show("Reverse transcription failed: sequence is not RNA.")
                    else:
                        self.__dnkController.add_seq(SequenceModel(new_seq))
                        self.show("Reverse transcribed RNA -> DNA.")
                        self.show_sequence()
            elif choice == "5":
                seq = self.__dnkController.get_sequence()
                if not seq:
                    self.show("No sequence. Use option 1 to add one.")
                else:
                    new_seq = self.__dnkController.reverse_complement(seq)
                    if new_seq is None:
                        self.show("Reverse complement failed: invalid sequence.")
                    else:
                        self.__dnkController.add_seq(SequenceModel(new_seq))
                        self.show("Replaced with reverse complement.")
                        self.show_sequence()
            elif choice == "6":
                seq = self.__dnkController.get_sequence()
                if not seq:
                    self.show("No sequence. Use option 1 to add one.")
                else:
                    gc, length = self.__dnkController.gc_content(seq)
                    self.show(f"Length: {length}, GC%: {gc:.2f}%")
            elif choice == "7":
                seq = self.__dnkController.get_sequence()
                if not seq:
                    self.show("No sequence. Use option 1 to add one.")
                else:
                    self.show_sequence()
                    idx_str = self.prompt("Enter 1-based position to mutate: ").strip()
                    new_base = self.prompt("Enter new base (A/C/G/T/U): ").strip().upper()
                    try:
                        idx = int(idx_str) - 1
                    except ValueError:
                        self.show("Invalid position.")
                        continue
                    result = self.__dnkController.mutate_base(seq, idx, new_base)
                    if result is None:
                        self.show("Mutation failed (invalid index or base for sequence type).")
                    else:
                        self.__dnkController.add_seq(SequenceModel(result))
                        self.show("Sequence mutated.")
                        self.show_sequence()
            elif choice == "0":
                self.show("Exiting.")
                break
            else:
                self.show("Unknown option. Try again.")



