export const abi = {
	"ABI version": 2,
	"version": "2.2",
	"header": ["pubkey", "time", "expire"],
	"functions": [
		{
			"name": "constructor",
			"inputs": [
			],
			"outputs": [
			]
		},
		{
			"name": "initBounty",
			"inputs": [
				{"name":"open","type":"bool"},
				{"name":"deposit","type":"uint128"},
				{"name":"ghIssue","type":"string"}
			],
			"outputs": [
			]
		},
		{
			"name": "attemptBounty",
			"inputs": [
				{"name":"index","type":"uint256"},
				{"name":"bountyHunters","type":"address[]"},
				{"name":"pullRequest","type":"string"}
			],
			"outputs": [
			]
		},
		{
			"name": "assignBounty",
			"inputs": [
				{"name":"index","type":"uint256"},
				{"name":"bountyHunters","type":"address[]"}
			],
			"outputs": [
			]
		},
		{
			"name": "acceptOpportunity",
			"inputs": [
				{"name":"index","type":"uint256"},
				{"name":"pullRequest","type":"string"}
			],
			"outputs": [
			]
		},
		{
			"name": "queryOracle",
			"inputs": [
				{"name":"index","type":"uint256"}
			],
			"outputs": [
			]
		},
		{
			"name": "updateBountyStatus",
			"inputs": [
				{"name":"index","type":"uint256"},
				{"name":"state","type":"uint8"}
			],
			"outputs": [
			]
		},
		{
			"name": "payout",
			"inputs": [
				{"name":"index","type":"uint256"}
			],
			"outputs": [
			]
		},
		{
			"name": "withdrawBounty",
			"inputs": [
				{"name":"index","type":"uint256"}
			],
			"outputs": [
			]
		},
		{
			"name": "reassignBounty",
			"inputs": [
				{"name":"index","type":"uint256"}
			],
			"outputs": [
			]
		},
		{
			"name": "bounties",
			"inputs": [
			],
			"outputs": [
				{"components":[{"name":"status","type":"uint8"},{"name":"open","type":"bool"},{"name":"issuer","type":"address"},{"name":"amount","type":"uint128"},{"name":"githubIssue","type":"string"},{"name":"pullRequest","type":"optional(string)"},{"name":"assigned","type":"optional(address[])"}],"name":"bounties","type":"tuple[]"}
			]
		}
	],
	"data": [
	],
	"events": [
		{
			"name": "oracleQuery",
			"inputs": [
				{"components":[{"name":"status","type":"uint8"},{"name":"open","type":"bool"},{"name":"issuer","type":"address"},{"name":"amount","type":"uint128"},{"name":"githubIssue","type":"string"},{"name":"pullRequest","type":"optional(string)"},{"name":"assigned","type":"optional(address[])"}],"name":"bounty","type":"tuple"}
			],
			"outputs": [
			]
		}
	],
	"fields": [
		{"name":"_pubkey","type":"uint256"},
		{"name":"_timestamp","type":"uint64"},
		{"name":"_constructorFlag","type":"bool"},
		{"name":"ORACLE_ADDRESS","type":"address"},
		{"components":[{"name":"status","type":"uint8"},{"name":"open","type":"bool"},{"name":"issuer","type":"address"},{"name":"amount","type":"uint128"},{"name":"githubIssue","type":"string"},{"name":"pullRequest","type":"optional(string)"},{"name":"assigned","type":"optional(address[])"}],"name":"bounties","type":"tuple[]"}
	]
} as const