//import { Address, Contract, ProviderRpcClient } from "everscale-inpage-provider";
import { EverscaleStandaloneClient, SimpleKeystore } from "everscale-standalone-client/nodejs";
import { Contract, ProviderRpcClient, Signer, Address } from "locklift";
import { FactorySource } from "../build/factorySource";
import { readFileSync } from "fs";
import { resolve } from "path";
import { load } from 'ts-dotenv';

const env = load({
  SC_ADDRESS: String,
});


//Importing Abi
import { abi as ballotContractAbi } from "./bountyboard.abi";
let addyString = env.SC_ADDRESS
let addy = new Address(addyString);
const bountycontract = locklift.factory.getDeployedContract("bountyboard", addy);
async function updateBountyStatus() {
  const signer = (await locklift.keystore.getSigner("0"))!;
  const response = await bountycontract.methods
    .updateBountyStatus({ index: 0, state: 4 })
    .sendExternal({ publicKey: signer.publicKey });
  console.log(response);
}
updateBountyStatus().catch(error => {
  console.error("An error occurred:", error);
});
