# Base class
class Painting:
    def __init__(self, title, artist, year, style):
        self.title = title
        self.artist = artist
        self.year = year
        self.style = style

    def display_info(self):
        print(f"🎨 '{self.title}' by {self.artist} ({self.year}) - Style: {self.style}")

    def estimate_value(self):
        print(f"Estimating value of '{self.title}'... 📈")
        return len(self.artist) * 1000  # simple fake formula


# Subclass (Inheritance)
class DigitalPainting(Painting):
    def __init__(self, title, artist, year, style, resolution):
        super().__init__(title, artist, year, style)
        self.resolution = resolution

    # Override method (Polymorphism)
    def display_info(self):
        print(f"🖥️ Digital Painting: '{self.title}' by {self.artist} "
              f"({self.year}) - {self.style} [{self.resolution} resolution]")


# Create objects
p1 = Painting("Starry Night", "Vincent van Gogh", 1889, "Post-Impressionism")
p2 = DigitalPainting("Sunset Dream", "Alice Smith", 2021, "Abstract", "4K")

# Use methods
p1.display_info()
print("Estimated value:", p1.estimate_value(), "USD\n")

p2.display_info()
print("Estimated value:", p2.estimate_value(), "USD")
