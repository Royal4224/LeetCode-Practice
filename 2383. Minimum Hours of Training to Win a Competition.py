class Solution:

    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy,
                         experience) -> int:
        hours_needed = 0
        for i in range(len(energy)):
            en = energy[i]
            exp = experience[i]

            if initialExperience <= exp:
                hours_needed += exp + 1 - initialExperience

                initialExperience = exp + 1

            if initialEnergy <= en:
                hours_needed += en + 1 - initialEnergy
                initialEnergy = en + 1

            initialExperience += exp
            initialEnergy -= en

        return hours_needed
    