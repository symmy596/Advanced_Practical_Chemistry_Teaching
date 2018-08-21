# Lesson Plan

### Week 1 - Introduction to Molecular Dynamics

Computational chemistry is often used in undergraduate laboratory exercises as a "black box". However, this is likely to reduce student engagement, as while the application is clear, the unlying mechanics are not. The first week of this practical will be focused on refreshing material from the second year "Introduction to computational chemistry" (CH20238) lecture module by allowing the students to interact directly with atomistic molecular dynamics simulations using the pylj software [1].

#### Learning Outcomes

- Understand the concepts of the Lennard-Jones potential and how it can be used in the modeling of atomic particles.
- Describe the Coulomb potential, and its importance in the modeling of ionic systems.
- Recognise the *recipe* associated with a molecular dynamics simulation.
- Be able to build a molecular dynamics simulation, using the pylj framework.
- Utilise the molecular dynamics simulation to study a system deviating from ideal gas behaviour.

#### Lesson Plan

The will be a self-led workshop where students will (in their own time) be able to work through an interactive Jupyter notebook, which will detail the mechanism of atomistic simulation. At the end, the students will use the pylj framework to build a simple molecular dynamics simulation and use this to preform a straight-forward application of molecular dynamics. This application will involve running simulations at a series of different atomic densities to reflect on the effect of density on a *typical* ideal gas system.

##### Assesment

- This week will form the basis for the methodology portion of the students report.

### Week 2 - Introduction to Transport Properties

The transport proerties of a material are crucial for many modern technologies, from batteries/fuel cells to nuclear materials. Week two of this practical will allow students to apply their understanding of molecular dynamics simulations, from week one, and apply it to some *real world* applications. The students will run molecular dynamics simulations on fluorite (CaF<sub>2</sub>), and analyse the transport properties of the material.

#### Learning Outcomes

- Understanding of the importance of mean squared displacement, and its relavance to molecular simulation.
- Application of first year kinetics to computational chemistry, by the investigation of the Arrhenius relation for transport in CaF<sub>2</sub>.

#### Lesson Plan

The students will run a molecular dynamics simulation of CaF<sub>2</sub> before running through a Jupyter notebook tutorial detailing how a mean squared displacment may be determined. Following this the molecular dynamics simulation will be repeated at a series of different temperatures, with the mean square displacement determined each time and the data used to investigate the Arrhenius relationship.

#### Assesment

- Mean squared displacement and Arrhenius relationship theory will form part of the methodology portion of the students report.
- The data measured will form components of the students' results.

### Week 3 - Defect Chemistry

As with people, no material is without defects. There are two main types of defect that exist in materials,
- Frenkel defects -- an atom is displaced in the lattice to an interstitial site; creaing a vacancy,
- Schottky defects -- a formula unit is missing from the lattice, creating (usually) a pair of vacancies.

Week 3 will see the students introducing Frenkel and Schottky defects to their CaF<sub>2</sub> configurations from the previous week. They will determine the effect that these defects have on the transport properties studied previously. In this week the students are expected to apply the skills that they have learned in Weeks 1 and 2 to design their own simulations.

#### Learning Outcomes

- Understanding of the nature of Frenkel and Schottky defects.
- Rationisation of the effect that such defects have on the transport properties of a material.

#### Lesson Plan

This process of this week ultimately lays with the student. However, the expectation is that the students will add cation Frenkel defects to the CaF<sub>2</sub> in different quantities assessing the impact on transport properties. The same will then be conducted with Schottky defects.

#### Assesment

- Key Report Question - How do Frenkel/Schottky defects affect the transport properties?

### Week 4 - Dopants

The doping of a material with different elements in order to obtain a desired property is now common practice, particularly for fuel cell materials, for example CeO<sub>2</sub> is doped with Gd<sup>3+</sup> to improve the oxygen transport, and therefore conductivity of the material. In this final week, students will investigate how the doping of cations into the CaF<sub>2</sub> structure affects the transport properties. Is it possible to increase the diffusion coefficient over the undoped material.

#### Learning Outcomes

- Assess the effect of dopant atoms on the properties of CaF<sub>2</sub>.
- Understand the role of the computational scienctist in materials discovery and development.

#### Lesson Plan

As with week three, this process ultimately lays with the student. The expectation is that the student will select four or five relevant cations to add to the CaF<sub>2</sub> structure and determine the diffusion coefficient of each.

#### Assesment

- Key Report Question - How do dopants affect the tranport properties?   

### Summary

Over the 4 weeks, the students will transition from a being lead through and introduction to molecular dynamics and shown how to run molecular simulation to being able to research independently the properties of a material. Week one will focus on the underlaying theory of molecular simulation, week two will introduce the students to the process of running molecular dynamics simulations. While, in weeks three and four the students are expected to independently apply this knowledge to design simulation that answer questions common to computational chemists.

### References

1. McCluskey et al., (2018). pylj: A teaching tool for classical atomistic simulation . Journal of Open Source Education, 1(2), 19, https://doi.org/10.21105/jose.00019
