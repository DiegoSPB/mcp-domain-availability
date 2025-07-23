#!/usr/bin/env python3

import sys
import json
import argparse
from mcp_domain_availability.main import check_domain

def main():
    parser = argparse.ArgumentParser(description='Check domain availability')
    parser.add_argument('domain_name', help='Domain to check')
    parser.add_argument('--domain', action='store_true', required=True, help='Domain check flag')
    parser.add_argument('--tlds', nargs='+', help='Specific TLDs to check (e.g., --tlds com ai tech)')
    
    if len(sys.argv) < 2:
        parser.print_help()
        return
    
    args = parser.parse_args()
    
    domain_query = f"{args.domain_name} --domain"
    if args.tlds:
        domain_query += f" --tlds {' '.join(args.tlds)}"
    
    result = check_domain(domain_query)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
