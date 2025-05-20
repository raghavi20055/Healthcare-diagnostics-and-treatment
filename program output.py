=== Performance Evaluation ===

Test 1: Input=['fever', 'cough', 'sore throat'] | Expected=flu | Got=flu => PASS
Test 2: Input=['fever', 'dry cough', 'tiredness', 'loss of taste'] | Expected=covid-19 | Got=covid-19 => PASS
Test 3: Input=['fever', 'chills', 'sweating', 'headache'] | Expected=malaria | Got=malaria => PASS
Test 4: Input=['fever', 'headache', 'muscle pain', 'rash'] | Expected=dengue | Got=dengue => PASS
Test 5: Input=['fever', 'abdominal pain', 'weakness', 'loss of appetite'] | Expected=typhoid | Got=typhoid => PASS
Test 6: Input=['fever', 'nausea', 'vomiting'] | Expected=None | Got=None => PASS

Accuracy: 100.00% (6/6 correct)
