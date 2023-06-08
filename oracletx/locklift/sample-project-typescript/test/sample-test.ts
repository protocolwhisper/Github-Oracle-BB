import { expect } from "chai";
import { Contract, Signer } from "locklift";
import { FactorySource } from "../build/factorySource";

let sample: Contract<FactorySource["bountyboard"]>;
let signer: Signer;

describe("Test Sample contract", async function () {
  before(async () => {
    signer = (await locklift.keystore.getSigner("0"))!;
  });
  describe("Contracts", async function () {
    it("Load contract factory", async function () {
      const sampleData = await locklift.factory.getContractArtifacts("bountyboard");

      expect(sampleData.code).not.to.equal(undefined, "Code should be available");
      expect(sampleData.abi).not.to.equal(undefined, "ABI should be available");
      expect(sampleData.tvc).not.to.equal(undefined, "tvc should be available");
    });

    it("Deploy contract", async function () {
      const INIT_STATE = 0;
      const { contract } = await locklift.factory.deployContract({
        contract: "bountyboard",
        publicKey: signer.publicKey,
        initParams: {},
        constructorParams: {},
        value: locklift.utils.toNano(2),
      });
      sample = contract;

      expect(await locklift.provider.getBalance(sample.address).then(balance => Number(balance))).to.be.above(0); // This checks the balance of the created contract
    });

    it("initBounty", async function () {
      const githuburl = "https://github.com/protocolwhisper/UNI-BOT-/issues/1";

      const response = await sample.methods
        .initBounty({ open: true, deposit: 2, ghIssue: githuburl })
        .sendExternal({ publicKey: signer.publicKey });

      // const response = await sample.methods.getDetails({}).call(); i think whis is to call a view function

      expect(response.output).to.exist;
    });

    it("updatestatus", async function () {
      const response = await sample.methods
        .updateBountyStatus({ index: 0, state: 3 })
        .sendExternal({ publicKey: signer.publicKey }); // Set this as completed
      //console.log(response.transaction)

      // const response = await sample.methods.getDetails({}).call(); i think whis is to call a view function
      expect(response.output).to.exist;
    });
  });
});
