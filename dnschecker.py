
import dns.resolver

result = dns.resolver.resolve('fontys.nl', 'A')


for val in result:
    print('A Record : ', val.to_text())
