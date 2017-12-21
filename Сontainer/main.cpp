#include <iostream>
#include <fstream>

class Counter {
    public:
        Counter();
        double getResult();

        friend std::istream& operator>>(std::istream& input_data, Counter& counter);
        friend std::ostream& operator<<(std::ostream& output_data, Counter& counter);

    private:
        void update(double first_number, int second_number);
        double result;
};

Counter::Counter(): result(0.0) {}

void Counter::update(double first_number, int second_number) {
    result += first_number * second_number;
}

std::istream& operator>>(std::istream& input_data, Counter& counter) {
    double first_number = 0;
    int second_number = 0;

    if (input_data >> first_number >> second_number) {
        counter.update(first_number, second_number);
        return input_data;
    }

    double result = counter.getResult();
    return input_data >> result;
}

std::ostream& operator<<(std::ostream& output_data, Counter& counter) {
    return output_data << "---> Current value: " << counter.getResult();
}

double Counter::getResult() {
    return result;
}

int main() {
    Counter counter;
    while (std::cin >> counter) {
        std::cout << counter << std::endl;
    }
    std::cout << "\n### That's all! ###" << std::endl;
    return 0;
}
